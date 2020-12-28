from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from user.forms import UserForm, ChangeMajorForm, FindPwdForm, LoginForm
from django.contrib.auth.forms import SetPasswordForm

from django.views import View
from django.urls import reverse
from .models import User
import jwt
import json
from .text import signup_message, change_pwd_message
from config.my_settings import EMAIL
from config.settings import SECRET_KEY

from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode 
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def index(request):
    return render(request,"index.html")


class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64)) #userid 디코딩
            user = User.objects.get(pk=uid)
            user_dic = jwt.decode(token,SECRET_KEY,algorithm='HS256')   #token을 SECRET_KEY를 활용하여 디코딩
            if user.id == user_dic["user"]:
                user.is_active = True
                user.save()
                return redirect("user:email_auth_confirm")

            return JsonResponse({'message':'auth fail'}, status=400)    #추후 수정
        except ValidationError:
            return JsonResponse({'message':'type_error'}, status=400)   #추후 수정
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)  #추후 수정

def login(request):
    """
    로그인
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=request.POST['email'])
            if user:
                password = request.POST['password']
                user = user[0]
                user = authenticate(request, username = user.username, password = password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('user:index')
                else:
                    form.add_error('password',"비밀번호가 일치하지 않습니다.")
            else:
                form.add_error('email',"존재하지 않는 계정입니다.")
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form':form})

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = User.objects.get(username=form.cleaned_data.get('username')) # 유저객체 받아오기
            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = jwt.encode({'user':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')   #토큰 생성
            message_data = signup_message(domain, uidb64, token)   #메세지 생성

            mail_title = "BooKU 가입을 환영합니다! 이메일 인증을 완료해주세요!"
            mail_to = user.email
            email = EmailMessage(mail_title, message_data, from_email='booku@BooKU.com',to=[mail_to])
            email.send()
            return redirect('user:email_auth_notice')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})


def email_auth_notice(request):
    """
    이메일 인증 요구
    """
    return render(request, 'user/email_auth_notice.html')

def email_auth_confirm(request):
    """
    이메일 인증 완료
    """
    return render(request, 'user/email_auth_confirm.html')


# def edit_info(request):
#     """
#     학과변경
#     """
    
#     if request.method == "POST":
#         user = User.objects.get(username=request.user)
#         form = EditForm(request.POST)
#         if form.is_valid():
#             user.first_major = form.cleaned_data['first_major']
#             user.second_major = form.cleaned_data['second_major']
#             user.third_major = form.cleaned_data['third_major']
#             user.save()
#             return redirect('user:login')
#     elif request.user.is_authenticated:
#         user = User.objects.get(username=request.user)
#         form = EditForm(instance = user)
#         return render(request, 'user/edit_info.html', {'form': form})
#     else:
#         return redirect('user:login')


def find_pwd(request):
    """
    비밀번호 찾기
    """
    if request.method == 'POST':
        form = FindPwdForm(request.POST)
        if form.is_valid():
            try:                 #해당 이메일이 db에 존재하면
                user = User.objects.get(email= form.cleaned_data['email'])
                current_site = get_current_site(request)
                domain = current_site.domain
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = jwt.encode({'user':user.id},SECRET_KEY,algorithm='HS256').decode('utf-8')   #토큰 생성
                message_data = change_pwd_message(domain, uidb64, token)   #메세지 생성

                mail_title = "BooKU 비밀번호를 잊으셨나요?"
                mail_to = user.email
                email = EmailMessage(mail_title, message_data, from_email='booku@BooKU.com',to=[mail_to])
                email.send()
                return HttpResponse("작성해주신 이메일로 비밀번호 변경 링크가 전송되었습니다. 이메일을 확인해주세요!")
            except User.DoesNotExist:   #없는 사용자인 경우
                return HttpResponse("존재하지 않는 이메일입니다.")
        else:
            return render(request, 'user/find_pwd.html', {'form':form})
    else:
        form=FindPwdForm()
        return render(request, 'user/find_pwd.html', {'form':form})




class Change_pwd(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64)) #userid 디코딩
            user = User.objects.get(pk=uid)
            user_dic = jwt.decode(token,SECRET_KEY,algorithm='HS256')   #token을 SECRET_KEY를 활용하여 디코딩
            if user.id == user_dic["user"]:
                authenticate(username=user.username, password= user.password)
                return redirect("user:change_pwd")

            return HttpResponse("auth fail") #JsonResponse({'message':'auth fail'}, status=400)    #추후 수정
        except ValidationError:
            return HttpResponse("type_error") #JsonResponse({'message':'type_error'}, status=400)   #추후 수정
        except KeyError:
            return HttpResponse("INVALID_KEY") #JsonResponse({'message':'INVALID_KEY'}, status=400)  #추후 수정

# @login_required(login_url='user:login')
# def change_pwd(request):
#     """
#     비밀번호 변경
#     """
#     if request.method == "POST":
#         form = SetPasswordForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('user:login')
#         else:
#             return HttpResponse("폼 에러")
#     else:
#         form = SetPasswordForm(request.user)
#         return render(request, 'user/change_pwd.html', {'form': form})


@login_required(login_url='user:login')
def change_major(request):
    """
    학과변경
    """
    if request.method =="POST":
        form = ChangeMajorForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'user/change_major.html', {'form':form})
    else:
        
        form =  ChangeMajorForm(instance=request.user)
    return render(request, 'user/change_major.html', {'form':form})

@login_required(login_url='user:login')
def change_account_info(request):
    """
    개인정보변경
    """
    return render(request, 'user/change_account_info.html')

@login_required(login_url='user:login')
def change_pwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 변경되었습니다!')
            return redirect('user:change_pwd')
        else:
            messages.error(request, '잘못된 입력입니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_pwd.html', {
        'form': form
    })