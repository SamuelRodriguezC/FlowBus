from rest_framework import serializers # type: ignore
from .models import Bus, Seat
from django.contrib.auth.models import User 

# Sreializador de usuarios para permirit el registro desde la API
class UserSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True) # La contraseña no se expone en las respuestas 
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
class BusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bus
        fields = '__all__'
        
        
class SeatSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Seat
        fields = ['id', 'seat_number', 'is_booked']