from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('about-us/', views.aboutus, name='about'),
    path('contact-us/', views.contactus, name='contact'),
]