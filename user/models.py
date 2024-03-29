from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import datetime


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active = True')

        return self._create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    MAJOR_CHOICES = [
        ('국어국문학과', '국어국문학과'),
        ('영어영문학과', '영어영문학과'),
        ('중어중문학과', '중어중문학과'),
        ('철학과', '철학과'),
        ('사학과', '사학과'),
        ('지리학과', '지리학과'),
        ('미디어커뮤니케이션학과', '미디어커뮤니케이션학과'),
        ('문화컨텐츠학과', '문화컨텐츠학과'),
        ('수학과', '수학과'),
        ('물리학과', '물리학과'),
        ('화학과', '화학과'),
        ('건축학부', '건축학부'),
        ('사회환경공학부', '사회환경공학부'),
        ('기계항공학부', '기계항공학부'),
        ('전기전자공학부', '전기전자공학부'),
        ('화학공학부', '화학공학부'),
        ('컴퓨터공학부', '컴퓨터공학부'),
        ('산업경영공학부 산업공학과', '산업경영공학부 산업공학과'),
        ('산업경영공학부 신산업융합학과', '산업경영공학부 신산업융합학과'),
        ('생물공학과', '생물공학과'),
        ('k뷰티산업융합학과', 'k뷰티산업융합학과'),
        ('정치외교학과', '정치외교학과'),
        ('경제학과', '경제학과'),
        ('행정학과', '행정학과'),
        ('국제무역학과', '국제무역학과'),
        ('응용통계학과', '응용통계학과'),
        ('융합인재학과', '융합인재학과'),
        ('글로벌비즈니스학과', '글로벌비즈니스학과'),
        ('경영학과', '경영학과'),
        ('기술경영학과', '기술경영학과'),
        ('부동산학과', '부동산학과'),
        ('미래에너지공학과', '미래에너지공학과'),
        ('스마트운행체공학과', '스마트운행체공학과'),
        ('스마트ICT융합공학과', '스마트ICT융합공학과'),
        ('화장품공학과', '화장품공학과'),
        ('줄기세포재생공학과', '줄기세포재생공학과'),
        ('의생명공학과', '의생명공학과'),
        ('시스템생명공학과', '시스템생명공학과'),
        ('융합생명공학과', '융합생명공학과'),
        ('생명과학특성학과', '생명과학특성학과'),
        ('동물자원과학과', '동물자원과학과'),
        ('식량자원공학과', '식량자원공학과'),
        ('축산식품생명공학과', '축산식품생명공학과'),
        ('식품유통공학과', '식품유통공학과'),
        ('환경보건과학과', '환경보건과학과'),
        ('산림조경학과', '산림조경학과'),
        ('수의예과', '수의예과'),
        ('수의학과', '수의학과'),
        ('커뮤니케이션디자인학과', '커뮤니케이션디자인학과'),
        ('산업디자인학과', '산업디자인학과'),
        ('의상디자인학과', '의상디자인학과'),
        ('리빙디자인학과', '리빙디자인학과'),
        ('현대미술학과', '현대미술학과'),
        ('영상영화학과', '영상영화학과'),
        ('일어교육과', '일어교육과'),
        ('수학교육과', '수학교육과'),
        ('체육교육과', '체육교육과'),
        ('음악교육과', '음악교육과'),
        ('교육공학과', '교육공학과'),
        ('영어교육과', '영어교육과'),
        ('교직과', '교직과'),
    ]

    first_major = models.CharField(
        max_length=30,
        choices=MAJOR_CHOICES,
        default=''
    )

    second_major = models.CharField(
        max_length=30,
        choices=MAJOR_CHOICES,
        default='',
        blank=True,
    )

    third_major = models.CharField(
        max_length=30,
        choices=MAJOR_CHOICES,
        default='',
        blank=True,
    )

    is_active = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False)

    objects = UserManager()

    def make_major_choices(self):
        major_choices = (
            ('all', '전체'),
            ('major1', self.first_major),
            ('major2', self.second_major),
            ('major3', self.third_major),
        )
        return major_choices
