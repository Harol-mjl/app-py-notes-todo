from rest_framework import serializers
from apps.users.models.user import User

class UserFieldsSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="full_name")

    class Meta:
        model = User
        fields = ["id", "label"]