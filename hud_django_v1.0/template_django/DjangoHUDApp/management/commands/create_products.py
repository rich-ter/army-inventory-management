from django.core.management.base import BaseCommand
from DjangoHUDApp.models import Product

class Command(BaseCommand):
    help = 'Creates all the product instances'

    def handle(self, *args, **options):

        # dides_products = [
        #     {'name': 'ΚΕΠΙΚ ΓΕΕΘΑ', 'image': None, 'category': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'usage': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'description': ''},
        #     {'name': 'ΚΕΠΙΚ ΓΕΣ', 'image': None, 'category': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'usage': 'ΚΑΜΙΑ ΕΠΙΛΟΓΗ', 'description': ''},
        # ]

        # for product_data in dides_products:
        #     Product.objects.get_or_create(**product_data)

        # self.stdout.write(self.style.SUCCESS('Successfully created products for doriforika'))

        doriforika_products = [
            {"batch_number": 751, "name": "ΤΕΧΝΙΚΑ ΕΓΧΕΙΡΙΔΙΑ", "unit_of_measurement": "Τεμάχια"},
            {"batch_number": 798, "name": "Τ.Δ.FD177/RACAL/PRM4720B", "unit_of_measurement": "Τεμάχια"},
            {"batch_number": 1005, "name": "MINI LINK ROUTERBOARD 2X16 db(MIKROTIK)", "unit_of_measurement": "Τεμάχια"},
            {"batch_number": 1509, "name": "ΤΡΟΦΟΔΟΤΙΚΟ ΜΕΚΑΛΩΔΙΟ ΣΥΝΔΕΣ", "unit_of_measurement": "Τεμάχια"},
            {"batch_number": 1521, "name": "ΚΑΛΩΔΙΟ ΤΕΤΡΑΠΟΛΙΚΟ", "unit_of_measurement": "Μέτρα"},
        ]

        # Create Product objects using doriforika_products data
        for data in doriforika_products:
            Product.objects.create(category='ΚΑΜΙΑ ΕΠΙΛΟΓΗ', usage='ΔΟΡΥΦΟΡΙΚΑ', description='', **data)

        self.stdout.write(self.style.SUCCESS('Products created successfully'))



