from django.core.management.base import BaseCommand
from ylika_app.models import Apothiki

class Command(BaseCommand):
    help = 'Creates Apothiki instances'

    def handle(self, *args, **options):
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΚΕΠΙΚ', perigrafi='Description 1', simioseis='Location 1')
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΤΑΓΜΑΤΟΣ', perigrafi='Description 2', simioseis='Location 2')
        Apothiki.objects.create(onoma='ΑΠΟΘΗΚΗ ΔΟΡΥΦΟΡΙΚΩΝ', perigrafi='Description 3', simioseis='Location 3')

        self.stdout.write(self.style.SUCCESS('Successfully created Apothiki instances'))
