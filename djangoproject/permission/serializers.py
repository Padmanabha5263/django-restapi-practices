from rest_framework import serializers

class PercustomerSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=12)
    email = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=25)