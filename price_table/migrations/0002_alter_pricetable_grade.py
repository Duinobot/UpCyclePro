# Generated by Django 4.0.6 on 2023-01-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricetable',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('P', 'Parts')], max_length=1),
        ),
    ]
