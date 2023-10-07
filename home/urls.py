from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.index),
    path('', views.HomeView.as_view(template_name='pages/home.html'), name = 'home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(template_name='articledetails/home.html'), name = 'articledetails'),
    path('contact/',views.contact, name = 'contact'),
    path('register/', views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name='pages/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name = 'logout')
]
