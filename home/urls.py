from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('customer_scan/<int:tag_number>', views.customer_scan, name='customer_scan'),
]