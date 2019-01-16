from django.urls import path
from . import views

app_name = 'core'

urlpatterns=[
    path('', views.RegistrationView, name='register' ),
    path('login/', views.LoginView, name='login'),
    path('login/success/', views.successLogin, name='login-success'),

]