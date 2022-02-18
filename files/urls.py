from unicodedata import name
from django.urls import path
from .views import HomeView,VideoView,ImageView,ChangeLanView

app_name = 'file'
urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('change_lang/',ChangeLanView.as_view(),name = 'change_lang'),
    path('gallery/video/',VideoView.as_view(),name = 'video'),
    path('gallery/image/',ImageView.as_view(),name = 'image'),
    
]