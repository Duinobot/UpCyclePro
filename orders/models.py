from django.db import models

# Create your models here.
# order
class Order(models.Model):
    # order id
    order_id = models.CharField(max_length=100)
    # user
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # order status
    order_status = models.CharField(max_length=100)
    # order date
    order_date = models.DateTimeField(auto_now_add=True)
    # order total
    order_total = models.IntegerField()
    # order quantity
    order_quantity = models.IntegerField()
    # order address
    order_address = models.CharField(max_length=100)
    # order city
    order_city = models.CharField(max_length=100)
    # order state
    order_state = models.CharField(max_length=100)
    # order zip code
    order_zip_code = models.CharField(max_length=100)
    # order phone number
    order_phone_number = models.CharField(max_length=100)
    # order email
    order_email = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id