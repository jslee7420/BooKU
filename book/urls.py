from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views
from .views import BookList, BookCreate, BookDelete, BookDetail, BookUpdate, search, update_deal, book_new,get_first_major_list,get_second_major_list,get_third_major_list

app_name = "book"

urlpatterns = [
    path("create/", BookCreate.as_view(), name='create'),
    #path("create/", book_new, name='create'),
    path("delete/<int:pk>/", BookDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BookUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", BookDetail.as_view(), name='detail'),

    path("", BookList.as_view(), name='index'),
    path("major1", get_first_major_list, name='major1'),
    path("major2", get_second_major_list, name='major2'),
    path("major3", get_third_major_list, name='major3'),

    path("search/", search, name='search'),
    path("detail/<int:pk>/update_deal/", update_deal, name='update_deal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

