from django.urls import path
from tokenauthenticationapp.views import peopleView

urlpatterns = [
    path("", peopleView, name="listpeoples"),
]
