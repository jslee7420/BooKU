from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import Activate

app_name = 'user'

urlpatterns = [
    # Login and SignUp
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),

    # My Page
    path('my_page/', views.my_page, name='my_page'),
    path('change_pwd', views.change_pwd, name='change_pwd'),
    path('change_major/', views.change_major, name='change_major'),
    path('change_username/', views.change_username, name='change_username'),
    path('my_posts/', views.my_posts, name='my_posts'),


    # Terms of service and privacy policy static pages
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    path('practice/', views.practice, name='practice')
]
