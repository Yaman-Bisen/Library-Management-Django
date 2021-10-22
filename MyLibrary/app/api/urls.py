from django.urls import path, include
from app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('crud',views.BookViewSet, basename='book')

urlpatterns = [
    path('',include(router.urls))
]
