# Generated by Django 2.1.5 on 2019-04-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190227_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Data Clerk'), (2, 'Health Official'), (3, 'Doctor')], null=True),
        ),
    ]