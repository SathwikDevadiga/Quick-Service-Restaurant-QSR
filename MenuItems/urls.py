from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuItemDetail.as_view(), name='menu_items'),
    path('<int:pk>/', views.MenuItemDetailView.as_view(), name='menu_item_detail'),
    path('available/', views.AvailableMenuItemsView.as_view(), name='available_menu_items'),
]