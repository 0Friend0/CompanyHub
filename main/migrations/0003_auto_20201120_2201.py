# Generated by Django 3.1.2 on 2020-11-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201120_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='name',
            new_name='supplier_name',
        ),
    ]
