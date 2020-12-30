from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Activate, Change_pwd

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),
    path('find_pwd/', views.find_pwd, name='find_pwd'),
    path('change_pwd/<str:uidb64>/<str:token>', Change_pwd.as_view()),
    path('change_pwd', views.change_pwd, name='change_pwd'),
    path('email_auth_notice/', views.email_auth_notice, name='email_auth_notice'),
    path('email_auth_confirm/', views.email_auth_confirm, name='email_auth_confirm'),
    path('change_major/', views.change_major, name='change_major'),
    path('change_account_info/',views.change_account_info, name='change_account_info'),
    path('change_username/', views.change_username, name='change_username'),
]