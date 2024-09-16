from django.urls import path
from . import views
urlpatterns = [
    path('sunil_login/', views.sunil_login, name='sunil_login'),
    path('sunil_home/', views.sunil_home, name='sunil_home'),
    path('add_employee/', views.add_employee, name='add_employee'),
]