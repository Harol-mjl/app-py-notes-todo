import django_filters
from django_filters import CharFilter

from apps.users.models import User

class UserFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    is_active = django_filters.BooleanFilter()
    first_name = CharFilter()
    last_name = CharFilter()
    email = CharFilter()

    class Meta:
        model = User
        fields = ['created_at', 'is_active', 'first_name', 'last_name', 'email']
