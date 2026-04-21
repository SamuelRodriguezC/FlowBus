# Verifica si las credenciales (usuario y contraseña) son válidas.
# Devuelve el objeto User si son correctas, o None si fallan.
from django.contrib.auth import authenticate  

# Permiso de DRF que permite el acceso solo a usuarios autenticados.
# Se usa en permission_classes dentro de vistas.
from rest_framework.permissions import IsAuthenticated  

# Modelo que representa el token de autenticación asociado a un usuario.
# Se utiliza para autenticación basada en Token (Token Authentication).
from rest_framework.authtoken.models import Token  

# status: contiene constantes para códigos HTTP (HTTP_200_OK, HTTP_404_NOT_FOUND, etc.).
# generics: provee vistas genéricas listas para CRUD (ListAPIView, CreateAPIView, etc.).
from rest_framework import status, generics  

# Clase base para crear vistas API personalizadas en DRF.
# Permite definir manualmente métodos como get(), post(), put(), delete().
from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import UserRegisterSerializer

class RegisterView(APIView): 
    def post(self, request): 
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user = user)
            return Response({'token':token.key}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView): 
    def post(self, request): 
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username, password = password)
        
        if user: 
            token, created = Token.objects.get_or_create(user = user)
            return Response({
                'token':token.key,
                'user_id': user.id
            }, status  = status.HTTP_200_OK)
        else: 
            return Response({'error': 'Invalid Credentials'}, status = status.HTTP_401_UNAUTHORIZED)