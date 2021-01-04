from django.http import request, HttpResponse

from django.shortcuts import redirect, render
from django.urls import reverse
from .models import CustomUser, ProfileImage
from django.contrib import auth

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from uuid import uuid4

# GET & POST
def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse('user:login'))
        else:
            return render(request, 'sign/login.html', {'login_false': '아이디나 비밀번호가 일치하지 않습니다😥'})

    return render(request, 'pages/user/login.html')


# GET 
def logout(request):
    auth.logout(request)
    return redirect('/')


# GET
def show(request, id):
    user_detail = CustomUser.objects.get(id=id)
    return render(request, 'user/show.html', {'user_detail':user_detail})


# GET & POST
def create(request):
    token = uuid4().hex
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user_email    = request.POST['username']
        user = CustomUser.objects.create_user(
            username=username, 
            password=password, 
            email=user_email, 
            is_active=False,
            active_token=token
            )
        
        # request를 보낸 사이트를 알려준다.
        current_site = get_current_site(request) 
        message = render_to_string(
            'user/user_active_email.html',
            {
            'user':user.id,
            'domain':current_site.domain,
            'token':token
            })
        mail_subject = "[Tripo] 회원가입 인증 메일입니다."
        user_email = user.username
        email = EmailMessage(mail_subject, message, to=[user_email])
        email.send()

        return HttpResponse(
                '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                'justify-content: center; align-items: center;">'
                '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                '</div>'
            )

    return render(request, 'pages/user/create.html')


#GET & POST
def create_userinfo(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.user.nickname:
        return redirect('/')

    if request.POST:
        user = CustomUser.objects.get(id=request.user.id)
        user.nickname = request.POST['nickname']
        user.save()
        return redirect('/')

    return render(request, 'pages/user/create_userinfo.html')


# GET & POST
def update(request, id):
    return render(request, 'pages/user/update.html')


# GET
def delete(request, id):
    return redirect('/')


def activate(request):
    id = request.GET['id']
    token = request.GET['token']
    print(id)
    print(token)
    user = CustomUser.objects.get(id=id)
    if user.active_token == token:
        print('인증완료')
        user.is_active = True
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('pages/users/create/userinfo')
    else:
        return HttpResponse('비정상적인 접근입니다.')