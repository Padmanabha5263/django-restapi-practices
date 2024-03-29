from django.shortcuts import render
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tokenauthenticationapp.models import Peoples
from tokenauthenticationapp.serializers import peopleSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def peopleView(request):
    peoplesobj = Peoples.objects.all()
    serializer = peopleSerializer(peoplesobj, many=True)
    return Response(serializer.data)