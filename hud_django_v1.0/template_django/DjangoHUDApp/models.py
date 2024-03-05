from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.contrib import admin




class Recipient(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=150, null = True)
    location = models.CharField(max_length=150, null = True)
    notes = models.CharField(max_length=450, null = True)

    def __str__(self):
	    return self.name

class Product(models.Model):

    PRODUCT_CATEGORY = (
        ("ΔΡΟΜΟΛΟΓΗΤΗΣ", "ΔΡΟΜΟΛΟΓΗΤΗΣ"), 
        ("CONVERTER", "CONVERTER"),
        ("SWITCH", "SWITCH"),
        ("MODULE", "MODULE"),
        ("ΜΕΤΑΤΡΟΠΕΑΣ", "ΜΕΤΑΤΡΟΠΕΑΣ"),
        ("LAN EXTENDER", "LAN EXTENDER"),
        ("ΚΑΛΩΔΙΩΣΗ", "ΚΑΛΩΔΙΩΣΗ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),
    )

    PRODUCT_USAGE = (
        ("ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ", "ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ"), 
        ("ΣΔΑ ΠΥΡΣΕΙΑ", "ΣΔΑ ΠΥΡΣΕΙΑ"),
        ("ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ", "ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ"),
        ("ΚΡΥΠΤΟ", "ΚΡΥΠΤΟ"),
        ("UPS", "UPS"),
        ("ΛΟΙΠΑ ΥΛΙΚΑ", "ΛΟΙΠΑ ΥΛΙΚΑ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),       
    )

    
    name = models.CharField(max_length=100, null = False)
    #maybe i will need to change the location below 
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    serial_number = models.CharField(max_length=100, null = True)
    category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    usage = models.CharField(max_length=50, choices=PRODUCT_USAGE, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    description = models.CharField(max_length=200, null=True)

    def stock_by_warehouse(self):
        return Stock.objects.filter(product=self).values('warehouse__name', 'quantity')
    
    def total_stock(self):
        return Stock.objects.filter(product=self).aggregate(total=Sum('quantity'))['total'] or 0
    
    def __str__(self):
	    return f"{self.name} - {self.category}"
    
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name} - Qty: {self.quantity}"

class Shipment(models.Model):
    SHIPMENT_TYPE_CHOICES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shipments')
    shipment_type = models.CharField(max_length=3, choices=SHIPMENT_TYPE_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.get_shipment_type_display()} - {self.date}"
    
    def save(self, *args, **kwargs):
        if self.shipment_type == 'IN':
            # Fetch the existing recipient named "ΤΔΒ 487"
            tdb_487 = Recipient.objects.get(name='ΤΔΒ 487')
            self.recipient = tdb_487
        super().save(*args, **kwargs)

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


class ShipmentItem(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, related_name='shipment_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - Qty: {self.quantity} in {self.shipment}"
