from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
] # Add this line to map the root URL

