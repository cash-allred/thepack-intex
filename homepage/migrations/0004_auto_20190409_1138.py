# Generated by Django 2.1.5 on 2019-04-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20190409_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='drugType',
            new_name='isOpioid',
        ),
    ]
