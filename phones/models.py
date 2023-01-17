from django.db import models
from orders.models import Order
# import ValidationError
from django.core.exceptions import ValidationError


# Create your models here.
class PhoneModel(models.Model):
    model = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.model

    # unique field: model
    class Meta:
        unique_together = ('model',)


class PhoneColor(models.Model):
    color = models.CharField(max_length=100)
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.color} ({self.phonemodel})"
    
    # unique together fields: color, phonemodel
    class Meta:
        unique_together = ('color', 'phonemodel') 


class PhoneStorage(models.Model):
    # storage option: 16, 32, 64, 128, 256, 512 GB, 1 TB
    storage = models.CharField(max_length=100, choices=[('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB'), ('512GB', '512GB'), ('1024TB', '1024TB')])
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.storage} ({self.phonemodel})"

    # unique together fields: storage, phonemodel
    class Meta:
        unique_together = ('storage', 'phonemodel')


class Phone(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(blank=True)
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    imei = models.CharField(max_length=100)

    price_table = models.ForeignKey('price_table.PriceTable', on_delete=models.CASCADE, null=True, blank=True)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE, null=True, blank=True)

    image = models.ImageField(upload_to='phones/images/', blank=True)
    description = models.TextField(blank=True)

    # date created, date updated, data sold
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=[('A', 'Available'), ('S', 'Sold'), ('R', 'Reserved')], default='A')

    # cost_price, sold_price, selling_price
    cost_price = models.IntegerField(null=True, blank=True)
    sold_price = models.IntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)


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

    # color and storage must have the same phonemodel as the phone
    def clean(self):
        if self.color.phonemodel != self.phonemodel:
            raise ValidationError('Color must belong to specific Model')
        if self.storage.phonemodel != self.phonemodel:
            raise ValidationError('Storage must belong to specific Model')