# Generated by Django 4.0.6 on 2023-01-04 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_phone_status_alter_phonecolor_unique_together_and_more'),
        ('price_table', '0003_alter_pricetable_unique_together'),
        ('listings', '0002_alter_listing_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_table.pricetable'),
        ),
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('model', 'storage', 'color', 'grade')},
        ),
        migrations.RemoveField(
            model_name='listing',
            name='selling_price',
        ),
    ]
