from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Creates user groups and users, then assigns users to groups'

    def handle(self, *args, **options):
        # Create groups
        group_dides, _ = Group.objects.get_or_create(name='ΔΙΔΕΣ')
        group_doriforika, _ = Group.objects.get_or_create(name='ΔΟΡΥΦΟΡΙΚΑ')
        
        # Define user data
        user_data = [
            {'username': 'alexandris', 'password': 'alexandris', 'group': group_doriforika},
            {'username': 'tsaprounis', 'password': 'tsaprounis', 'group': group_dides},
            {'username': 'nikolaidis', 'password': 'nikolaidis', 'group': group_dides},
            {'username': 'raftogiannis', 'password': 'raftogiannis', 'group': group_dides},
        ]

        # Create users and assign to groups
        for user_info in user_data:
            user, created = User.objects.get_or_create(username=user_info['username'])
            if created:
                user.set_password(user_info['password'])
                user.save()
                user.groups.add(user_info['group'])
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username} and added to {user_info["group"].name}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user.username} already exists'))
