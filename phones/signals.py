from listings.models import Listing
from price_table.models import PriceTable
from .models import Phone, PhoneModel, PhoneStorage, PhoneColor
#import all
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# auto generate slug(imei) for Phone
def pre_save_phone(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.imei)

pre_save.connect(pre_save_phone, sender=Phone)

# when phone is created, Create Listing if combinattion of Mdoel storage, grade is not in Listings
# create PriceTable if combination of Model, storage, grade is not in PriceTable
def post_save_phone(sender, instance, created, *args, **kwargs):
    if created:
        # check if combination of model, storage, grade is in Listings
        if not Listing.objects.filter(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade).exists():
            # if not, create new Listing
            Listing.objects.create(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade)
        # check if combination of model, storage, grade is in PriceTable
        if not PriceTable.objects.filter(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade).exists():
            # if not, create new PriceTable
            PriceTable.objects.create(phonemodel=instance.phonemodel, storage=instance.storage, grade=instance.grade)

post_save.connect(post_save_phone, sender=Phone)

# auto generate slug for PhoneModel
def pre_save_phone_model(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_phone_model, sender=PhoneModel)

# auto generate slug(model name + color) for PhoneColor
def pre_save_phone_color(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.phonemodel.name + instance.name)

pre_save.connect(pre_save_phone_color, sender=PhoneColor)

# auto generate slug(model name + storage) for PhoneStorage
def pre_save_phone_storage(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.phonemodel.name + instance.storage)

pre_save.connect(pre_save_phone_storage, sender=PhoneStorage)