from rest_framework.serializers import ModelSerializer
from .models import User, DealerStatus


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'dealer_status']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # hash password
        instance.save()
        return  instance


class DealerStatusSerializer(ModelSerializer):
    class Meta:
        model = DealerStatus
        fields = ['__all__']