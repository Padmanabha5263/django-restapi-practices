from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from application1.serializer import CustomerSerializer
from application1.models import Cusomter
# Create your views here.

@api_view(["GET"])
def customersview(request):
    customers = Cusomter.objects.all()
    serializers = CustomerSerializer(customers, many=True)
    return Response(serializers.data)