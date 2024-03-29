from django.contrib import admin
from application1.models import Cusomter
from permission.models import PerCustomer
# Register your models here.

admin.site.register(Cusomter)
admin.site.register(PerCustomer)