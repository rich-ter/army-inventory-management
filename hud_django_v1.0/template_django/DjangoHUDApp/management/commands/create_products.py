from django.core.management.base import BaseCommand
from DjangoHUDApp.models import Product

class Command(BaseCommand):
    help = 'Creates all the product instances'

    def handle(self, *args, **options):

        dides_products = [
            {'name': 'ΚΕΠΙΚ ΓΕΕΘΑ', 'image': None, 'category': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'usage': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'description': ''},
            {'name': 'ΚΕΠΙΚ ΓΕΣ', 'image': None, 'category': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'usage': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'description': ''},
        ]

        for product_data in dides_products:
            Product.objects.get_or_create(**product_data)

        self.stdout.write(self.style.SUCCESS('Successfully created products for doriforika'))

        doriforika_products = [
            {'name': 'ΚΕΠΙΚ ΓΕΕΘΑ', 'image': None, 'category': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'usage': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'description': ''},
            'ΚΕΠΙΚ ΓΕΣ',
        ]

        for entry in doriforika_products:
            Product.objects.get_or_create(name=entry, contact_person='', location='', notes='')

        self.stdout.write(self.style.SUCCESS('Successfully imported Recipients '))



# class Product(models.Model):

#     PRODUCT_CATEGORY = (
#         ("ΔΡΟΜΟΛΟΓΗΤΗΣ", "ΔΡΟΜΟΛΟΓΗΤΗΣ"), 
#         ("CONVERTER", "CONVERTER"),
#         ("SWITCH", "SWITCH"),
#         ("MODULES", "MODULES"),
#         ("ΜΕΤΑΤΡΟΠΕΑΣ", "ΜΕΤΑΤΡΟΠΕΑΣ"),
#         ("LAN EXTENDER", "LAN EXTENDER"),   
#         ("ΚΑΛΩΔΙΩΣΗ", "ΚΑΛΩΔΙΩΣΗ"),
#         ("ΛΟΙΠΑ ΥΛΙΚΑ", "ΛΟΙΠΑ ΥΛΙΚΑ"),
#         ("IP PHONES", "IP PHONES"),
#         ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),
#     )

#     PRODUCT_USAGE = (
#         ("ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ", "ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ"), 
#         ("ΣΔΑ ΠΥΡΣΕΙΑ", "ΣΔΑ ΠΥΡΣΕΙΑ"),
#         ("ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ", "ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ"),
#         ("ΚΡΥΠΤΟ", "ΚΡΥΠΤΟ"),
#         ("UPS", "UPS"),
#         ("ΔΟΡΥΦΟΡΙΚΑ", "ΔΟΡΥΦΟΡΙΚΑ"),
#         ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),       
#     )

#     name = models.CharField(max_length=100, null = False)
#     #maybe i will need to change the location below 
#     image = models.ImageField(upload_to='product_images/', blank=True, null=True)
#     # serial_number = models.CharField(max_length=100, null = True)
#     category = models.CharField(max_length=30, choices=PRODUCT_CATEGORY, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
#     usage = models.CharField(max_length=50, choices=PRODUCT_USAGE, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
#     description = models.CharField(max_length=200, null=True)
