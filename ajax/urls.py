from django.urls import path
from . import views
urlpatterns = [
    path('generate_tag', views.generate_tag, name='generate_tag'),
]