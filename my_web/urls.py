
from django.urls import path
from my_web import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/<int:pk>/', views.create_order, name='create_order'),
    path('get_products/', views.get_products, name='get_products'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
]
