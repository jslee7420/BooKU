from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('activate/<str:uidb64>/<str:token>', views.Activate.as_view()),
]