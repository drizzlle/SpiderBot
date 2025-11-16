from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ScrapeView, ChatView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('scrape/', ScrapeView.as_view(), name='scrape'),
    path('chat/', ChatView.as_view(), name='chat'),
]