from django.db import models
from phones.models import PhoneModel, PhoneStorage
from listings.models import Listing
from django.db.models.signals import pre_save

# Create model for price table, with the following fields:
# - model
# - storage
# - grade
# - price
class PriceTable(models.Model):
    model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100)
    price = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.model.name + ' ' + self.storage.storage + 'GB [' + self.grade + ' Grade]'


# when PriceTable price is updated, filter out listings with the same model, storage and grade, update the selling price in Listing model
def update_listing_price(sender, instance, *args, **kwargs):
    listings = Listing.objects.filter(model=instance.model, storage=instance.storage, grade=instance.grade)
    for listing in listings:
        listing.selling_price = instance.price
        listing.save()

pre_save.connect(update_listing_price, sender=PriceTable)