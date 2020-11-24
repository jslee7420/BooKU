from django.db import models
from django.urls import reverse
from config import settings
from user.models import User

class AllBook(models.Model):
    STATE_CHOICES =(
        ('A','아주좋음'),
        ('B', '좋음'),
        ('C', '보통'),
        ('D', '나쁨'),
    )
    DEAL_FLAG = 1 #거래중이면 1, 거래완료면 0
    deal = "거래중"
    unmajor =""

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_user')
    title = models.TextField(verbose_name='제목', max_length=50, null=False)
    lecture = models.CharField(verbose_name='수업', max_length=50, null=True)
    text = models.TextField(verbose_name='게시글',null=False)

    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='timeline_all_post/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kakaoUrl = models.URLField(default='', help_text='생성한 오픈 카카오톡 링크를 작성해 주세요')

    class Meta:
        ordering = ['-created']

    def checkDeal(self):
        if(self.DEAL_FLAG==1):
            self.deal = "거래완료"
            return 1
        elif(self.DEAL_FLAG==0):
            self.deal = "거래중"
            return 0

    def get_absolute_url(self):
        return reverse('book:detail', args=[self.id])

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)

