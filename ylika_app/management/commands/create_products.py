from django.core.management.base import BaseCommand
from ylika_app.models import Proion

class Command(BaseCommand):
    help = 'Creates Apothikes & KEPIK (Paraliptes) instances'

    def handle(self, *args, **options):

        # Create Paraliptis instances if they don't exist
        products_list = [
            "CISCO 871",
            "CISCO 1751",
            "CISCO 2600",
            "CISCO 3600",
            "PANDATEL 64 Kbps",
            "Combiner",
            "CISCO 2911",
            "CISCO 1941",
            "CISCO 1921",
            "ALCATEL SWITCH 48 Port",
            "SWITCH 2960C - 8TC-S",
            "SWITCH 2960C - 24TC-S",
            "Κάρτα HWIC – 1ADSL",
            "Κάρτα HWIC - 1T",
            "Κάρτα WIC - 1T (Παλαιού τύπου)",
            "Κάρτα WIC - 2T",
            "Κάρτα VIC 3 – 4 FXS / DID",
            "Κάρτα VIC 3 – 2 FXS / DID",
            "Κάρτα VIC 3 – 4 FXS / DID",
            "Κάρτα VIC 3 – 2 FXS / DID",
            "Κάρτα VIC 2– 2 FXO",
            "Κάρτα VIC 2– 4 FXO",
            "Κάρτα EHWIC – 4 ESG",
            "Κάρτα PVDM 3-16",
            "Κάρτα PVDM 2-8",
            "Τροφοδοτικά Cisco 2800",
            "Κάρτα BRI 8B- S/T",
            "Κάρτα WIC 1 AM V2",
            "Κάρτα 1B- S/T",
            "FAST ETHERNET MEDIA CONVERTER",
            "Allied Telesis Extended Ethernet",
            "ALCATEL ROUTER",
            "Καλώδια Τροφοδοσίας",
            "Καλώδια κονσόλας",
            "Καλώδια V35-Smart serial",
            "Καλώδια X21-Smart serial",
            "Καλώδια RS530-Smart serial",
            "Καλώδια RS232-Smart serial",
            "Καλώδια BNC - RJ 45",
            "Racks",
            "PANDATEL",
            "PANDACOM",
            "Μετατροπείς G703-X21",
            "VTC LIFESIZE 50",
            "Ανυψωτήρες Rack"
        ]

        for product in products_list:
            Proion.objects.get_or_create(onoma=product)

# Given the provided list, we will create a Python list with the name products_list



        self.stdout.write(self.style.SUCCESS('Successfully imported proion entries'))

