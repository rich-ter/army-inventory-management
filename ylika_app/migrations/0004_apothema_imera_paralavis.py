# Generated by Django 5.0 on 2024-01-19 08:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ylika_app', '0003_alter_proion_xrisi'),
    ]

    operations = [
        migrations.AddField(
            model_name='apothema',
            name='imera_paralavis',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
