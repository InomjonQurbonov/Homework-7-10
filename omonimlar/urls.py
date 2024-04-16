from django.urls import path, include
from .views import OmonimlarViewSet, OmonimlarListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'omonimlar', OmonimlarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('omonimlar-list/', OmonimlarListView.as_view())
]
