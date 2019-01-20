from django.urls import path
from . import views

app_name = 'core'

urlpatterns=[
    path('', views.RegistrationView, name='register' ),
    path('login/', views.LoginView, name='login'),
    path('login/success/', views.successLogin, name='login-success'),
    path('profile/<str:user_name>/', views.displayUserProfile, name='user_profile_page'),
    path('profile/<str:user_name>/edit/',views.editProfile,name = "edit_profile"),
    path('profile/logout/', views.userLogout , name="logout"),

]