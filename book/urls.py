from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views
from .views import BookCreate, BookDelete, BookDetail, BookUpdate, update_deal, bookList

app_name = "book"

urlpatterns = [
    path("", bookList, name='index'),
    path("detail/<int:pk>/", BookDetail.as_view(), name='detail'),

    path("create/", BookCreate.as_view(), name='create'),
    path("delete/<int:pk>/", BookDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BookUpdate.as_view(), name='update'),

    path("detail/<int:pk>/update_deal/", update_deal, name='update_deal'),

] + static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
