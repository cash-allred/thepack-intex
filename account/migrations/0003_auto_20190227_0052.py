# Generated by Django 2.1.5 on 2019-02-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_favcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favcolor',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]
