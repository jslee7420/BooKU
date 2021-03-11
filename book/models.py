from typing import Tuple
from django.db import models
from django.urls import reverse
from config import settings
from user.models import User
from django.contrib.auth import get_user_model


def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return username


def get_login_user(request):
    return request.user


class Book(models.Model):
    STATE_CHOICES = (
        ('최상', '최상'),
        ('상', '상'),
        ('보통', '보통'),
        ('하', '하'),
    )

    #user = get_user_model()
    writer = models.CharField(max_length=50, null=True, verbose_name='저자')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    title = models.TextField(verbose_name='제목', max_length=50, null=False)
    lecture = models.CharField(verbose_name='수업', max_length=50, null=True)
    text = models.TextField(verbose_name='게시글', null=False)

    state = models.CharField(
        max_length=10, choices=STATE_CHOICES, verbose_name='도서 상태')
    price = models.PositiveIntegerField(default=0, verbose_name='가격')
    image = models.ImageField(
        upload_to='timeline_post/%Y/%m/%d', blank=True, null=True, verbose_name='이미지')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # , choices=user.make_major_choices())
    major_category = models.CharField(max_length=40, verbose_name='전공 카테고리')
    kakaoUrl = models.URLField(
        default='', help_text='생성한 오픈 카카오톡 링크를 작성해 주세요', verbose_name='오픈채팅 주소')
    deal_flag = models.BooleanField(default=1)  # 거래중이면 1, 거래완료면 0

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('book:detail', args=[self.id])

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)
