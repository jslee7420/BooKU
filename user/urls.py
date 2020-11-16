from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Activate

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),
    path('edit_info/',views.edit_info, name='edit_info'),
]