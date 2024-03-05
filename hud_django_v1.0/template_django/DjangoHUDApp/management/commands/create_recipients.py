from django.core.management.base import BaseCommand
from DjangoHUDApp.models import Warehouse, Recipient

class Command(BaseCommand):
    help = 'Creates Apothikes & KEPIK (Paraliptes) instances'

    def handle(self, *args, **options):
        # Create Apothiki instances if they don't exist
        # apothiki_objects = [
        #     {'onoma': 'ΑΠΟΘΗΚΗ ΚΕΠΙΚ', 'perigrafi': 'Description 1', 'simioseis': 'Location 1'},
        #     {'onoma': 'ΑΠΟΘΗΚΗ ΤΑΓΜΑΤΟΣ', 'perigrafi': 'Description 2', 'simioseis': 'Location 2'},
        #     {'onoma': 'ΑΠΟΘΗΚΗ ΔΟΡΥΦΟΡΙΚΩΝ', 'perigrafi': 'Description 3', 'simioseis': 'Location 3'},
        # ]

        # for apothiki_data in apothiki_objects:
        #     Apothiki.objects.get_or_create(**apothiki_data)

        # self.stdout.write(self.style.SUCCESS('Successfully created Apothiki instances'))

        # Create Paraliptis instances if they don't exist
        entries = [
            'ΚΕΠΙΚ ΓΕΕΘΑ',
            'ΚΕΠΙΚ ΓΕΣ',
            'ΚΕΠΙΚ 1 ΣΤΡΑΤΙΑ',
            'ΚΕΠΙΚ Γ ΣΣ',
            'ΚΕΠΙΚ 10 ΣΠ',
            'ΚΕΠΙΚ 8 ΜΠ ΤΑΞ',
            'ΚΕΠΙΚ 9 ΜΠ ΤΑΞ',
            'ΚΕΠΙΚ 15 ΣΠ',
            'ΚΕΠΙΚ 1 ΣΠ',
            'ΚΕΠΙΚ II Μ/Κ ΜΠ',
            'ΚΕΠΙΚ 33 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ 34 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ Δ ΣΣ',
            'ΚΕΠΙΚ 29 Μ/Π ΤΑΞ',
            'ΚΕΠΙΚ 50 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ XII Μ/Κ ΜΠ',
            'ΚΕΠΙΚ 31 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ 7 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ XXIII ΤΘΤ',
            'ΚΕΠΙΚ XVI Μ/Κ ΜΠ',
            'ΚΕΠΙΚ 30 Μ/Κ ΤΞ',
            'ΚΕΠΙΚ 3 Μ/Κ ΤΑΞ',
            'ΚΕΠΙΚ ΤΔ/21 ΣΠ',
            'ΚΕΠΙΚ XX ΤΘΜ',
            'ΚΕΠΙΚ XXIV ΤΘΤ',
            'ΚΕΠΙΚ XXI ΤΘΤ',
            'ΚΕΠΙΚ XXV ΤΘΤ',
            'ΚΕΠΙΚ ΤΔ/41 ΣΠ',
            'ΚΕΠΙΚ ΑΣΔΕΝ',
            'ΚΕΠΙΚ 5 Α/Μ ΤΑΞ',
            'ΚΕΠΙΚ 79 ΑΔΤΕ',
            'ΚΕΠΙΚ ΔΑΝ ΙΚΑΡΙΑΣ',
            'ΚΕΠΙΚ 80 ΑΔΤΕ',
            'ΚΕΠΙΚ 88 ΣΔΙ',
            'ΚΕΠΙΚ 95 ΑΔΤΕ',
            'ΚΕΠΙΚ ΔΑΝ ΜΕΓΙΣΤΗΣ',
            'ΚΕΠΙΚ 96 ΑΔΤΕ',
            'ΚΕΠΙΚ 98 ΑΔΤΕ',
            'ΚΕΠΙΚ ΑΣΔΥΣ',
            'ΚΕΠΙΚ ΔΙΚΕ',
            'ΚΕΠΙΚ ΔΥΒ',
            'ΚΕΠΙΚ ΜΕΡΥΠ',
            'ΚΕΠΙΚ Ι ΜΠ',
            'ΚΕΠΙΚ 1 ΤΑΞΑΣ',
            'ΚΕΠΙΚ 1 ΤΑΞΚΔ-ΑΛ',
            'ΚΕΠΙΚ 32 ΤΑΞΠΝ',
            'ΚΕΠΙΚ 71 Α/Μ ΤΑΞ',
            'ΤΔΒ 487',
        ]

        for entry in entries:
            Recipient.objects.get_or_create(name=entry, contact_person='', location='', notes='')

        self.stdout.write(self.style.SUCCESS('Successfully imported Recipients '))


