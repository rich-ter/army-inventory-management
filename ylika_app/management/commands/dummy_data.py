from django.core.management.base import BaseCommand
from ylika_app.models import Proion, Paraliptis, Apothiki

class Command(BaseCommand):
    help = 'Creates Proion, Paraliptis, and Apothiki mock data'

    def handle(self, *args, **options):
        # Create Apothiki instances
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΚΕΠΙΚ', perigrafi='Description 1', simioseis='Location 1')
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΤΑΓΜΑΤΟΣ', perigrafi='Description 2', simioseis='Location 2')
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΔΟΡΥΦΟΡΙΚΩΝ', perigrafi='Description 3', simioseis='Location 3')

        # Create Proion instances
        Proion.objects.create(onoma='Proion 1', seriakos_arithmos='Serial 1', perigrafi='Description 1', typos_proiontos='Type 1')
        Proion.objects.create(onoma='Proion 2', seriakos_arithmos='Serial 2', perigrafi='Description 2', typos_proiontos='Type 2')
        Proion.objects.create(onoma='Proion 3', seriakos_arithmos='Serial 3', perigrafi='Description 3', typos_proiontos='Type 3')

        # Create Paralipti instances
        Paraliptis.objects.create(onoma='Paraliptis 1', monada='Monada 1')
        Paraliptis.objects.create(onoma='Paraliptis 2', monada='Monada 2')
        Paraliptis.objects.create(onoma='Paraliptis 3', monada='Monada 3')

        self.stdout.write(self.style.SUCCESS('Successfully created Apothiki, Proion, and Paralipti instances'))
