from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.contrib import admin
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Recipient(models.Model):
    commanding_unit = models.CharField(max_length=100)
    recipient_unit = models.CharField(max_length=100, default='None Specified')
    notes = models.CharField(max_length=450, null = True)

    def __str__(self):
	    return self.recipient_unit


class Product(models.Model):

    PRODUCT_CATEGORY = (
        ("ΔΡΟΜΟΛΟΓΗΤΗΣ", "ΔΡΟΜΟΛΟΓΗΤΗΣ"), 
        ("CONVERTER", "CONVERTER"),
        ("SWITCH", "SWITCH"),
        ("MODULES", "MODULES"),
        ("ΜΕΤΑΤΡΟΠΕΑΣ", "ΜΕΤΑΤΡΟΠΕΑΣ"),
        ("LAN EXTENDER", "LAN EXTENDER"),   
        ("ΚΑΛΩΔΙΩΣΗ", "ΚΑΛΩΔΙΩΣΗ"),
        ("ΛΟΙΠΑ ΥΛΙΚΑ", "ΛΟΙΠΑ ΥΛΙΚΑ"),
        ("IP PHONES", "IP PHONES"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),
    )

    PRODUCT_USAGE = (
        ("ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ", "ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ"), 
        ("ΣΔΑ ΠΥΡΣΕΙΑ", "ΣΔΑ ΠΥΡΣΕΙΑ"),
        ("ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ", "ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ"),
        ("ΚΡΥΠΤΟ", "ΚΡΥΠΤΟ"),
        ("UPS", "UPS"),
        ("ΔΟΡΥΦΟΡΙΚΑ", "ΔΟΡΥΦΟΡΙΚΑ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),       
    )

    MEASUREMENT_TYPES = (
        ("ΤΕΜΑΧΙΑ", "ΤΕΜΑΧΙΑ"), 
        ("ΜΕΤΡΑ", "ΜΕΤΡΑ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),       
    )

    name = models.CharField(max_length=100, null = False)
    batch_number = models.CharField(max_length=100, null = False, default='KAMIA EPILOGH')
    unit_of_measurement = models.CharField(max_length=30, choices=MEASUREMENT_TYPES, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    usage = models.CharField(max_length=50, choices=PRODUCT_USAGE, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    description = models.CharField(max_length=200, null=True)

    # def stock_by_warehouse(self):
    #     return Stock.objects.filter(product=self).values('warehouse__name', 'quantity')
    
    def total_stock(self):
        """Return the total stock across all warehouses for this product."""
        return self.stocks.aggregate(total=Sum('quantity'))['total'] or 0
    
    def __str__(self):
	    return f"{self.name} - {self.category}"
    

class ProductInstance(models.Model):
    PRODUCT_FUNCTIONALITY = [
        ('ΛΕΙΤΟΥΡΓΙΚΟ', 'ΛΕΙΤΟΥΡΓΙΚΟ'),
        ('ΥΠΟ ΕΛΕΓΧΟ', 'ΥΠΟ ΕΛΕΓΧΟ'),
        ('ΒΛΑΒΗ', 'ΒΛΑΒΗ'),
    ]

    PRODUCT_CHARGE = [
        ('ΧΡΕΩΜΕΝΟ', 'ΧΡΕΩΜΕΝΟ'),
        ('ΑΧΡΕΩΤΟ', 'ΑΧΡΕΩΤΟ'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='instances')
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField(null=True, blank=True)
    warranty_expiration = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"This is the product with id:{self.id} with the serial number{self.serial_number}"

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    access_groups = models.ManyToManyField(Group, related_name="access_warehouses")

    def __str__(self):
        return f"{self.name}"
    
class ShipmentItem(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='shipment_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - Qty: {self.quantity} in {self.shipment}"
    

@receiver(post_save, sender=ShipmentItem)
def adjust_stock_on_save(sender, instance, created, **kwargs):
    adjust_stock(instance, created=True)

@receiver(post_delete, sender=ShipmentItem)
def adjust_stock_on_delete(sender, instance, **kwargs):
    adjust_stock(instance, created=False)

def adjust_stock(instance, created):
    with transaction.atomic():
        stock, _ = Stock.objects.get_or_create(
            product=instance.product,
            warehouse=instance.warehouse,
            defaults={'quantity': 0}
        )

        # Determine the adjustment direction based on the shipment type
        if instance.shipment.shipment_type == 'IN':
            adjustment = instance.quantity if created else -instance.quantity
        elif instance.shipment.shipment_type == 'OUT':
            adjustment = -instance.quantity if created else instance.quantity

        # Apply the adjustment
        stock.quantity += adjustment

        # Prevent stock from going negative for 'OUT' shipments
        if stock.quantity < 0:
            raise ValidationError(f'Insufficient stock for {instance.product.name} in {instance.warehouse.name}. Cannot proceed with the operation.')

        stock.save()



class Shipment(models.Model):
    SHIPMENT_TYPE_CHOICES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    ]

    SHIPMENT_METHOD_CHOICES = [
        ('ΥΕΣΑ', 'ΥΕΣΑ'),
        ('ΚΡΥΠΤΟΔΙΑΥΛΟΣ', 'ΚΡΥΠΤΟΔΙΑΥΛΟΣ'),
        ('ΠΑΡΑΛΑΒΗ ΑΠΟ ΕΞΟΥΣΙΟΔΟΤΗΜΕΝΟ ΠΡΟΣΩΠΙΚΟ', 'ΠΑΡΑΛΑΒΗ ΑΠΟ ΕΞΟΥΣΙΟΔΟΤΗΜΕΝΟ ΠΡΟΣΩΠΙΚΟ'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shipments')
    shipment_type = models.CharField(max_length=3, choices=SHIPMENT_TYPE_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.get_shipment_type_display()} - {self.date}"
    

    # def save(self, *args, **kwargs):
    #     # Assign a default recipient for incoming shipments
    #     if self.shipment_type == 'IN' and not self.recipient_id:
    #         tdb_487, _ = Recipient.objects.get_or_create(name='ΤΔΒ 487')
    #         self.recipient = tdb_487

    #     # Call save first to ensure the Shipment instance has an ID
    #     super().save(*args, **kwargs)  

    #     # Adjust stock levels for shipment items within a transaction
    #     with transaction.atomic():
    #         for item in self.shipment_items.all():
    #             stock_qs = Stock.objects.filter(product=item.product, warehouse=item.warehouse)
    #             if self.shipment_type == 'IN':
    #                 stock_qs.update(quantity=F('quantity') + item.quantity)
    #             elif self.shipment_type == 'OUT':
    #                 # Check if there is enough stock before proceeding
    #                 if stock_qs.first().quantity < item.quantity:
    #                     raise ValidationError(f'Insufficient stock for {item.product.name}.')
    #                 stock_qs.update(quantity=F('quantity') - item.quantity)

        # THIS NEEDS TO BE FIXED - IT CHECKS IF ENOUGH STOCK FOR A PRODUT BEFORE SENDING 
    # def save(self, *args, **kwargs):
    #     with transaction.atomic():
    #         # First, validate all items can be fulfilled
    #         for item in self.shipment_items.all():
    #             stock = Stock.objects.get(product=item.product, warehouse=self.warehouse)
    #             if self.shipment_type == 'OUT' and item.quantity > stock.quantity:
    #                 raise ValidationError(f'Not enough stock for {item.product.name} to complete this shipment.')

    #         super().save(*args, **kwargs)  # Save the Shipment instance
            
    #         # Then, adjust stock quantities
    #         for item in self.shipment_items.all():
    #             stock, _ = Stock.objects.select_for_update().get_or_create(
    #                 product=item.product, 
    #                 warehouse=self.warehouse
    #             )
                
    #             if self.shipment_type == 'IN':
    #                 stock.quantity += item.quantity
    #             else:  # 'OUT'
    #                 stock.quantity -= item.quantity  # Already validated above
                
    #             stock.save()

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name} - Qty: {self.quantity}"
    


# implementing the different use roles and groups for 