from django.db.models.signals import pre_save
from django.utils.text import slugify
from listings.models import Listing


# update title and slug when Listing is saved
def pre_save_listing(sender, instance, *args, **kwargs):
    if not instance.title:
        instance.title = instance.phonemodel.model + ' ' + instance.storage.storage + ' [' + instance.color.color + ']' + ' [' + instance.grade + ' Grade]'
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_listing, sender=Listing)