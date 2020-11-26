from django.conf.urls import url
from django.urls import path
from .views import AllBookList, AllBookCreate, AllBookDelete, AllBookDetail, AllBookUpdate, search, complete_sale

app_name = "allbook"

urlpatterns = [
    path("create/", AllBookCreate.as_view(), name='create'),
    path("delete/<int:pk>/", AllBookDelete.as_view(), name='delete'),
    path("update/<int:pk>/", AllBookUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", AllBookDetail.as_view(), name='detail'),
    path("", AllBookList.as_view(), name='index'),
    path("search/", search, name='search'),
    path("complete/<int:pk>/", complete_sale, name='complete'),
]