from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    #Serializa nombres para testear como funca apiview.
    name = serializers.CharField(max_length=16)



class UserProfileSerializer(serializers.ModelSerializer):
    #Serializa un objeto de tipo "perfil de usuario".
    """La clase Meta es necesaria dentro de un serializador de objetos,
    dado que le enseña a donde apuntar a la clase en si."""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        """Extra kwargs nos permite establecer caracteristicas especiales
        a nuestros atributos."""
        extra_kwargs = {
            'password': {
                'write_only':'True',
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """crea y retorna un nuevo usuario"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password= validated_data['password']
        )
        return user



