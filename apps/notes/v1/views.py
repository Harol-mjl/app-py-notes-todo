from rest_framework import viewsets

from apps.notes.models.notes import Notes
from apps.notes.v1.serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer