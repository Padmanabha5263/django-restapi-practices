from rest_framework import serializers

class peopleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=40)
    phone=serializers.CharField(max_length=40)
    