from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_orders, name='get_orders'),
    path('new/', views.new_order, name='new_order'), 
    path('<str:pk>/', views.get_order, name='get_order'), 
    path('<str:pk>/process/', views.process_order, name='process_order'), 
    path('<str:pk>/delete/', views.delete_order, name='delete_order'), 
]