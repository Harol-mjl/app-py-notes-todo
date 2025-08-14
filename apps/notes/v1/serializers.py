from rest_framework import serializers
from apps.notes.models.notes import Notes
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = [
            'id',
            'title',
            'description',
            'active',
            'type',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']