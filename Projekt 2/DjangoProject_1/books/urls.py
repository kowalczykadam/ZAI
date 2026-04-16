from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import import_from_api, import_csv
from .api_views import BookViewSet

router = DefaultRouter()
router.register(r'api/books', BookViewSet)

urlpatterns = [
    path('import-api/', import_from_api, name='import_api'),
    path('import-csv/', import_csv, name='import_csv'),
] + router.urls
