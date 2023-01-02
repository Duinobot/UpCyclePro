from django.db import models
# import everything needed
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from orders.models import Order
from users.models import CustomUser
# Create your models here.
class PhoneModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class PhoneColor(models.Model):
    name = models.CharField(max_length=100)
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class PhoneStorage(models.Model):
    storage = models.CharField(max_length=100)
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.storage


class Phone(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100)

    price = models.IntegerField()
    image = models.ImageField(upload_to='phones/images/')
    description = models.TextField()

    # date created, date updated, data sold
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold_at = models.DateTimeField(null=True, blank=True)

    # cost_price, sold_price, selling_price
    cost_price = models.IntegerField()
    sold_price = models.IntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


    # phone grade (A, B, C, D, Parts)
    grade = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('P', 'Parts')])
    # test results, all default to 'Y' (Yes)
    
    # 1. power up
    power_up = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 2. touch screen
    touch_screen = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 3. lcd
    lcd = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 5. rear camera
    rear_camera = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 4. front camera
    front_camera = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 6. baseband
    baseband = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 7. wifi
    wifi_bluetooth = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 8. speaker
    speaker = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 9. microphone
    microphone = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 10. headphone jack
    headphone_jack = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 11. charging port
    charging_port = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 12. housing
    housing = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 13. frame
    frame = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 14. back glass
    back_glass = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 15. camera lens
    camera_lens = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 16. id sensor
    id_sensor = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    # 17. battery
    battery = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')

    def __str__(self):
        return self.name