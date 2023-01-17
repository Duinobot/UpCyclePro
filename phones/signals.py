from listings.models import Listing
from price_table.models import PriceTable
from .models import Phone, PhoneModel, PhoneStorage, PhoneColor
#import all
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.utils import timezone


# auto generate slug(imei) for Phone
def pre_save_phone(sender, instance, *args, **kwargs):
    if not instance.name:
        instance.name = instance.phonemodel.model + ' ' + instance.storage.storage + ' [' + instance.color.color + ']' + ' [' + instance.grade + ' Grade]'
    if not instance.slug:
        instance.slug = slugify(instance.name + " " + instance.imei)
    # when order field is assigned, update phone status to 'sold', and save the listing selling price to sold price
    if instance.order:
        instance.status = 'sold'
        instance.sold_price = instance.listing.selling_price
        # save sold_at to current time
        instance.sold_at = timezone.now()


pre_save.connect(pre_save_phone, sender=Phone)

# when phone is created, Create Listing if combinattion of Mdoel storage, grade is not in Listings
# create PriceTable if combination of Model, storage, grade is not in PriceTable
def post_save_phone(sender, instance, created, *args, **kwargs):
    if created:
        # check if combination of model, storage, grade is in PriceTable, if yes, get the PriceTable, if not, create new PriceTable
        instance.price_table, created = PriceTable.objects.get_or_create(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade)
        # check if combination of model, storage, grade, color is in Listings
        if not Listing.objects.filter(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade, color=instance.color).exists():
            # if not, create new Listing
            Listing.objects.create(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade, color=instance.color, price_table=instance.price_table)
        # save instance
        instance.save()

post_save.connect(post_save_phone, sender=Phone)

# auto generate slug for PhoneModel
def pre_save_phone_model(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.model)

pre_save.connect(pre_save_phone_model, sender=PhoneModel)

# auto generate slug(model + color) for PhoneColor
def pre_save_phone_color(sender, instance, *args, **kwargs):
    # change color to proper case
    instance.color = instance.color.title()
    if not instance.slug:
        instance.slug = slugify(instance.phonemodel.model + " " + instance.color)

pre_save.connect(pre_save_phone_color, sender=PhoneColor)

# auto generate slug(model + storage) for PhoneStorage
def pre_save_phone_storage(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.phonemodel.model + " " + instance.storage)

pre_save.connect(pre_save_phone_storage, sender=PhoneStorage)