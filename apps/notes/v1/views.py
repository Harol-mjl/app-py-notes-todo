from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.notes.models.notes import Notes
from apps.notes.v1.filters import NotesFilter
from apps.notes.v1.serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    filterset_class = NotesFilter
    filter_backends = (DjangoFilterBackend,)