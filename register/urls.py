from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register-reg'),
    path('login/', views.login, name='register-login'),
    path('logout/', views.logout, name='register-logout')
]
