from django.urls import path, include
from .views import place_order, signup_view, delete_order, order_history  # Import order_history view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),  
    path('reservation/', views.reservation, name='reservation'), 
    path('signup/', signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),  # URL pattern for order history
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.index, name='profile'),
]
