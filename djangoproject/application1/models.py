from django.db import models

# Create your models here.
class Cusomter(models.Model):
    customername=models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        db_table='customer'