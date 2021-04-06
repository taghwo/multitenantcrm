from django.urls import path
from . import views
urlpatterns = [
    path('login', views.LoginView.as_view(), name="auth-login"),
    path('logout', views.LogoutView.as_view(), name="auth-logout"),
    path('user', views.AuthUser.as_view(), name="auth-user"),
    path('register', views.RegisterView.as_view(), name="auth-register")
]
