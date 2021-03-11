from django import forms
from .models import Book
from user.models import User
from django.contrib.auth import get_user_model


# class BookForm(forms.Form, tuple):
#     STATE_CHOICES = (
#         ('A', '아주좋음'),
#         ('B', '좋음'),
#         ('C', '보통'),
#         ('D', '나쁨'),
#     )

#     user = get_user_model()

#     MAJOR_CHOICES = (
#         (all, '전체'),
#         ('first_major', user.first_major),
#         ('second_major', user.second_major),
#         ('third_major', user.third_major),
#     )

#     title = forms.CharField(max_length=50)
#     text = forms.CharField(widget=forms.Textarea)
#     lecture = forms.CharField(max_length=50)
#     #major_category = forms.Select(user.make_major_choices(self=get_user_model()))
#     major_category = forms.ChoiceField(widget=forms.Select(), choices=tuple)

#     image = forms.FileField()
#     #state = forms.Select(STATE_CHOICES)
#     state = forms.ChoiceField(widget=forms.Select(), choices=STATE_CHOICES)
#     price = forms.IntegerField()
#     kakaoUrl = forms.URLField(help_text='생성한 오픈 카카오톡 링크를 작성해 주세요')

#     def save(self, commit=True):
#         book = Book(**self.cleaned_data)
#         if commit:
#             book.save()
#         return book
