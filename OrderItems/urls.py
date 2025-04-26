from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderItemsDetails.as_view(), name='order_items'),
    
]