from rest_framework import serializers

from accounts.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'first_name', 'last_name','is_active']
        read_only_fields = ['id', 'is_active']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number', 'username']

    def create(self, validated_data): #used create_user so password is hashed
        return User.objects.create_user(**validated_data)


