from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from permission.models import PerCustomer
from permission.serializers import PercustomerSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def percustomerview(request, format=None):
    customersresponse = PerCustomer.objects.all()
    serializers = PercustomerSerializer(customersresponse, many=True)
    return Response(serializers.data)