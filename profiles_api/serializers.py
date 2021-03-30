from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #Serializa nombres para testear como funca apiview.
    name = serializers.CharField(max_length=16)
