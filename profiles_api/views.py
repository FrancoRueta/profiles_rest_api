from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    #Testeo de API view.

    def get(self, request, format=None):
        #Devuelve una lista de acciones de APIVIEW.
        an_apiview = [
            'Usa metodos HTTP como functions get,post,patch,put,delete)',
            'Es similar a un Django View normal.',
            'Otorga gran control sobre la logica de la APP',
            'Se mapea manualmente hacia URLs',
        ]
        return Response({'message': 'Hola!', 'an_apiview': an_apiview})
