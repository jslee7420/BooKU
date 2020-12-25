from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Activate, Change_pwd

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),
    # path('find_id/',views.find_id, name='find_id'),
    path('find_pwd/', views.find_pwd, name='find_pwd'),
    path('change_pwd/<str:uidb64>/<str:token>', Change_pwd.as_view()),
    path('edit_pwd', views.edit_pwd, name='edit_pwd'),
    path('find_id/', views.find_id, name='find_id'),
]