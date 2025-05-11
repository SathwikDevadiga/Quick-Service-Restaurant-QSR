from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderDetail.as_view(), name='orders'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('average-daily-sales/', views.AverageDailySalesView.as_view()),
    
]