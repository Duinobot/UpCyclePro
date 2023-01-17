# Generated by Django 4.0.6 on 2023-01-04 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0009_alter_phone_cost_price'),
        ('price_table', '0003_alter_pricetable_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetable',
            old_name='model',
            new_name='phonemodel',
        ),
        migrations.AlterUniqueTogether(
            name='pricetable',
            unique_together={('phonemodel', 'storage', 'grade')},
        ),
    ]