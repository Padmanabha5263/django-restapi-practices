from django.urls import path
from application1.views import customersview

urlpatterns = [
    path('',customersview, name="getallcustomers")
]
