# Generated by Django 4.0.6 on 2023-01-03 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('phonemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phonemodel')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('phonemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phonemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('imei', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='phones/images/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sold_at', models.DateTimeField(blank=True, null=True)),
                ('cost_price', models.IntegerField()),
                ('sold_price', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('P', 'Parts')], max_length=1)),
                ('power_up', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('touch_screen', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('lcd', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('rear_camera', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('front_camera', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('baseband', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('wifi_bluetooth', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('speaker', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('microphone', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('headphone_jack', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('charging_port', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('housing', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('frame', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('back_glass', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('camera_lens', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('id_sensor', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('battery', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phonecolor')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('phonemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phonemodel')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phonestorage')),
            ],
        ),
    ]