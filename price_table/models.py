from django.db import models

# Create model for price table, with the following fields:
# - model
# - storage
# - grade
# - price
class PriceTable(models.Model):
    phonemodel = models.ForeignKey('phones.PhoneModel', on_delete=models.CASCADE)
    storage = models.ForeignKey('phones.PhoneStorage', on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('P', 'Parts')])
    price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f"{self.phonemodel.model} {self.storage.storage} [{self.grade} Grade]"

    # Unique together fields: phonemodel, storage, grade
    class Meta:
        unique_together = ('phonemodel', 'storage', 'grade')