from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('notice_list/',views.notice_list,name="notice_list"),
    path('notice_detail/<int:notice_id>/', views.notice_detail, name="notice_detail"),
]