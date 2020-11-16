from django.urls import path
from .views import BookList, BookCreate, BookDelete, BookDetail, BookUpdate, search

app_name = "book"

urlpatterns = [
    path("create/", BookCreate.as_view(), name='create'),
    path("delete/<int:pk>/", BookDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BookUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", BookDetail.as_view(), name='detail'),
    path("", BookList.as_view(), name='index'),
    path("search/", search, name='search'),
]

