from listings.models import Listing
from django.db.models.signals import pre_save
from .models import PriceTable
from django.utils.text import slugify

# when PriceTable price is updated, filter out listings with the same model, storage and grade, update the selling price in Listing model
def update_listing_price(sender, instance, *args, **kwargs):
    # check if price exists
    if not instance.price:
        return
    listings = Listing.objects.filter(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade)
    for listing in listings:
        listing.selling_price = instance.price
        listing.save()

    # genereate slug for PriceTable
    if not instance.slug:
        instance.slug = slugify(instance.phonemodel.model + " " + instance.storage.storage + " " + instance.grade)

pre_save.connect(update_listing_price, sender=PriceTable)