from rest_framework import serializers

class NotesField(serializers.Field):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    active = serializers.BooleanField(default=True)
    type = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)

