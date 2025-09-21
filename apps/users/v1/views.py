from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from apps.users.models.user import User
from apps.users.v1.filters import UserFilter
from apps.users.v1.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter