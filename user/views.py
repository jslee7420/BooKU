from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import UserForm
from django.views import View
from django.urls import reverse
from .models import User
import jwt
import json
from .text import message
from config.my_settings import EMAIL
from config.settings import SECRET_KEY

from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode 
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text


class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64)) #userid 디코딩
            user = User.objects.get(pk=uid)
            user_dic = jwt.decode(token,SECRET_KEY,algorithm='HS256')   #token을 SECRET_KEY를 활용하여 디코딩
            if user.id == user_dic["user"]:
                user.is_active = True
                user.save()
                return redirect("user:login")

            return JsonResponse({'message':'auth fail'}, status=400)    #추후 수정
        except ValidationError:
            return JsonResponse({'message':'type_error'}, status=400)   #추후 수정
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)  #추후 수정



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
            message_data = message(domain, uidb64, token)   #메세지 생성

            mail_title = "BooKU 가입을 환영합니다! 이메일 인증을 완료해주세요!"
            mail_to = user.email
            email = EmailMessage(mail_title, message_data, from_email='booku@BooKU.com',to=[mail_to])
            email.send()

            return redirect('user:login')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})

