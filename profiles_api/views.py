from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


#RESUMEN RAPIDO: 
# *GET: Sirve para SACAR datos de nuestra BDD
# *POST: Sirve para GUARDAR datos en nuestra BDD
# *PUT: Sirve para ACTUALIZAR datos en nuestra BDD
# *PATCH: Sirve para ACTUALIZAR datos de forma PARCIAL.
# *DELETE: deletea :B


class HelloApiView(APIView):
    #Testeo de API view.
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        #Devuelve una lista de acciones de APIVIEW.

        an_apiview = [
            'Usa metodos HTTP como functions get,post,patch,put,delete)',
            'Es similar a un Django View normal.',
            'Otorga gran control sobre la logica de la APP',
            'Se mapea manualmente hacia URLs',
        ]
        return Response({'message': 'Hola!', 'an_apiview': an_apiview})

    
    def post(self, request):
        #Crea un saludo "Hola" con un nombre especifico.
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name.capitalize()}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None): #pk = primary key
        #Maneja la actualizacion de objetos.
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        #Maneja la actualizacion PARCIAL de objetos.
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        #Roba datos.
        return Response({'method':'DELETE'})
