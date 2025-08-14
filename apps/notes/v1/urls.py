from rest_framework import routers
from apps.notes.v1.views import NotesViewSet

router = routers.DefaultRouter()
router.register(r'notes', NotesViewSet, basename='notes')
urlpatterns = router.urls