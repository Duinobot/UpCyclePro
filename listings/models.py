from django.db import models
# import model, storage and color from phones app
from phones.models import PhoneModel, PhoneStorage, PhoneColor

# Create your models here.

# Create a Listing model, with the following fields:
# - title
# - description
# - model
# - storage
# - color
# - grade
# - selling_price
# - sku
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phonemodel = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('P', 'Parts')])
    price_table = models.ForeignKey('price_table.PriceTable', on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=100,blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    # Unique together fields: model, storage, color, grade
    class Meta:
        unique_together = ('phonemodel', 'storage', 'color', 'grade')

