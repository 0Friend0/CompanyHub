# Generated by Django 3.1.2 on 2020-11-29 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201120_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.supplier'),
        ),
    ]