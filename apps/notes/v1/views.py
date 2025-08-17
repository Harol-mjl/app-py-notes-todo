from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.notes.models.notes import Notes
from apps.notes.v1.filters import NotesFilter
from apps.notes.v1.serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    filterset_class = NotesFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    search_fields = ('id', 'title',)
    ordering_fields = ('id', 'type', 'updated_at', 'created_at')
    ordering = ('-updated_at', )