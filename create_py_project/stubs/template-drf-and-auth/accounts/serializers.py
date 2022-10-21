from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""

    name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("name", "email", "password", "re_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "re_password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user


class UpdatePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    oldpassword = serializers.CharField(required=True)
    newpassword = serializers.CharField(required=True, validators=[validate_password])


class GeneralSettingSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)

    class Meta:
        model = User
        fields = "email"
