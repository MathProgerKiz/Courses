from rest_framework import serializers
from User.models import UsersModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )

    def create(self, validated_data):
        user = UsersModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ("id", "username")