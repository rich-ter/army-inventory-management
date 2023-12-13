from django.contrib.auth.models import User, Group


#defining the various user groups
def create_groups():
    Group.objects.get_or_create(name='dides')
    Group.objects.get_or_create(name='ddb')
    Group.objects.get_or_create(name='aksip_kepik')


#creating users





#assigning user to a group.




