# Generated by Django 4.0.6 on 2023-01-04 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_phone_status_alter_phonecolor_unique_together_and_more'),
        ('price_table', '0002_alter_pricetable_grade'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pricetable',
            unique_together={('model', 'storage', 'grade')},
        ),
    ]