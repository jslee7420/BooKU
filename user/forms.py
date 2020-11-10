from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
    # email = forms.EmailField()
    # first_major = forms.Select()
    # second_major = forms.Select()
    # third_major = forms.Select()
    # date_of_birth = forms.DateField()
    # gender = forms.Select()
    
    class Meta:
        model = User
        fields = ("username", "email","first_major","second_major","third_major", "date_of_birth", "gender","password1","password2")
        labels = {
            "username":"아이디", 
            "email":"이메일",
            "first_major":"원전공",
            "second_major":"다/부전공1",
            "third_major":"다/부전공2", 
            "date_of_birth":"생년월일",
            "gender":"성별",
            "password1":"비밀번호",
            "password2":"비밀번호 재확인",
        }