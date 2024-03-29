from django.db import models

# Create your models here.
# table that contains customer data 
class PerCustomer(models.Model):
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email= models.CharField(max_length=50)
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="per_customer"