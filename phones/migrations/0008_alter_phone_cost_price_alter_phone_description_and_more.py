# Generated by Django 4.0.6 on 2023-01-04 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_alter_phonestorage_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='cost_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, upload_to='phones/images/'),
        ),
    ]
