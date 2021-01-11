from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from hospital.app.client.models import Shift, Client
from hospital.app.user.models import User



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name', )


class UserRegistrationSerializer(serializers.ModelSerializer):

    client = ClientSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'client',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        user = User.objects.create_user(**validated_data)

     
        Client.objects.create(
            user=user,
           client_name= client_data['client_name'],           
            
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }



class ShiftCreationSerializer(serializers.ModelSerializer):    
   

    class Meta:
        model = Shift
        fields = ('start', 'start_date', 'arrival_time', 'departure_time', 'repeat', 'shift_availability' )
#extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        shift = Shift.objects.create_shift(**validated_data)

        return shift
