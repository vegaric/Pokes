# Generated by Django 3.2.3 on 2021-08-27 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pokes_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cant',
            new_name='cant_pokes',
        ),
    ]
