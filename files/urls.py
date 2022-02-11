from django.urls import path
from .views import HomeView,VideoView

app_name = 'file'
urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('gallery/video/',VideoView.as_view(),name = 'video'),
]