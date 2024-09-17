from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
    path('customer_scan/<str:tag_number>', views.customer_scan, name='customer_scan'),
]