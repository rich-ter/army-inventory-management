from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Runs all the specified management commands in order'

    def handle(self, *args, **options):
        commands = [
            'create_recipients',
            'create_groups_users_warehouses',
            'create_doriforika_products',
            'create_kepik_products',
            'create_kepik_products_tsaprou'
        ]

        for command in commands:
            self.stdout.write(f'Running {command}...')
            try:
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f'Successfully ran {command}'))
            except CommandError as e:
                self.stdout.write(self.style.ERROR(f'Error running {command}: {e}'))
                raise CommandError(f'Error running {command}: {e}')

        self.stdout.write(self.style.SUCCESS('All commands have been executed successfully'))
