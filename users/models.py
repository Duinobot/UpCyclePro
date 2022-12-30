from django.db import models
# import everything needed
from django.contrib.auth.models import AbstractUser


# Create custom user model
class CustomUser(AbstractUser):
    # add additional fields in here
    pass