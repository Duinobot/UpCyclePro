# Generated by Django 4.0.6 on 2023-01-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_rename_model_listing_phonemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
