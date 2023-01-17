# Generated by Django 4.0.6 on 2023-01-03 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('order_status', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.IntegerField()),
                ('order_quantity', models.IntegerField()),
                ('order_address', models.CharField(max_length=100)),
                ('order_city', models.CharField(max_length=100)),
                ('order_state', models.CharField(max_length=100)),
                ('order_zip_code', models.CharField(max_length=100)),
                ('order_phone_number', models.CharField(max_length=100)),
                ('order_email', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
