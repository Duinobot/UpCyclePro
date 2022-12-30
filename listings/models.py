from django.db import models
# import model, storage and color from phones app
from phones.models import PhoneModel, PhoneStorage, PhoneColor
# import everything needed
from django.db.models.signals import pre_save
from django.utils.text import slugify

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
    model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100)
    selling_price = models.IntegerField()
    sku = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

# update title and slug when Listing is saved
def pre_save_listing(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = instance.model.name + ' ' + instance.storage.storage + 'GB [' + instance.color.name + ']' + ' [' + instance.grade + ' Grade]'
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_listing, sender=Listing)

# update PriceTable is selling_price is updated
def update_listing_price(sender, instance, *args, **kwargs):
    listings = Listing.objects.filter(model=instance.model, storage=instance.storage, grade=instance.grade)
    for listing in listings:
        listing.selling_price = instance.price
        listing.save()