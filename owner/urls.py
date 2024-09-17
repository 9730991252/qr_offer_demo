from django.urls import path
from . import views
urlpatterns = [
    path('office_home/', views.office_home, name='office_home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),
    path('profile/', views.profile, name='profile'),
    path('valid_to_date/', views.valid_to_date, name='valid_to_date'),
]