import django_filters
from django_filters import CharFilter

from apps.notes.models.notes import Notes


class NotesFilter(django_filters.FilterSet):
    type = CharFilter(field_name='type')

    class Meta:
        model = Notes
        fields = ['type']