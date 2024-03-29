from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_major", "second_major",
                  "third_major", "password1", "password2")
        labels = {
            "username": "아이디",
            "email": "이메일",
            "first_major": "원전공",
            "second_major": "다/부전공1",
            "third_major": "다/부전공2",
            "password1": "비밀번호",
            "password2": "비밀번호 재확인",
        }


class ChangeMajorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_major", "second_major", "third_major"]


class FindPwdForm(forms.Form):
    email = forms.EmailField(label='email')


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(max_length=20)


class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
