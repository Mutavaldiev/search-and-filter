
from django.urls import path
from my_web import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/<int:pk>/', views.create_order, name='create_order'),
    path('get_products/', views.get_products, name='get_products'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
]
