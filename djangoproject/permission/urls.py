from django.urls import path
from permission.views import percustomerview
urlpatterns = [
    path("",percustomerview, name="listallcustomers")
]
