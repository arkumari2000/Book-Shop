from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.Delete, name='delete'),
    path('deleteBook/<str:pk>/', views.DeleteBook, name='deleteBook'),
    path('updateBook/<str:pk>/', views.updateBook, name='updateBook'),
    path('deletecustomer/<str:pk>/', views.DeleteCustomer, name='deletecustomer'),
    path('order/<str:pk>/', views.order, name='order'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('newcustomer', views.newcustomer, name='newcustomer'),
    path('profile', views.profile, name='profile'),
    path('user', views.user, name='user'),
    path('register', views.register, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logOut, name='logout'),
]
