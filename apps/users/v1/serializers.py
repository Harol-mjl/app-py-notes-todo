from rest_framework import serializers
from apps.users.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'role',
            'phone',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']