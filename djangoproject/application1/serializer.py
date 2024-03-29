from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    customername=serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=12)
    email = serializers.CharField(max_length=50)