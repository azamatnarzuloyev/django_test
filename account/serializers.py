from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.models import User
class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id", "phone",
               "password", "shop_password",
           
        ]


class AuthenticationSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=12,
        min_length=12,
    )
    # password =  serializers.CharField(max_length=100)
    shop_password = serializers.CharField(max_length=200)

    def validate_phone(self, value):
        from re import match

        if not match("^998\d{2}\s*?\d{3}\s*?\d{4}$", value):
            raise serializers.ValidationError("Invalid phone number.")

        return value
    
class AUthouserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    phone = serializers.ReadOnlyField()
    
    class Meta:
        model = get_user_model()
        fields = [
            "id", "phone",
           "first_name", "last_name",
            "two_step_password",
          
        ]



class CreateTwoStepPasswordSerializer(serializers.Serializer):
    """
        Base serializer two-step-password.
    """
    new_password = serializers.CharField(
        max_length=20,
    )

    confirm_new_password = serializers.CharField(
        max_length=20,
    )

    def validate(self, data):
        password = data.get('new_password')
        confirm_password = data.get('confirm_new_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {"Error": "Your passwords didn't match."}
            )

        return data