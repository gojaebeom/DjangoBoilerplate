from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

"""
< CustomUser Model >
장고에서 지원하는 User 모델을 상속받아
새로운 column 들을 추가해줍니다.

nickname : 
장고의 User 모델은 first name과 last name 을 받는 column 이 존재합니다.
이 프로젝트에서는 닉네임을 추가로 사용하기 때문에 선언하였습니다.
active_token :
oauth 로그인을 사용하지 않고 일반 username 로그인을 사용하게 될 경우 
이메일 인증을 받는 방식을 사용합니다. 이때 active_token의 값을 비교하여 
이메일 인증이 정상적으로 처리되면 User 모델에 정의 되어 있는 is_active 칼럼을 활성화 시켜 
로그인 처리 시킵니다. 

< ProfileImage Model >
CustomUser 모델과 1:N 관계로 정의합니다.
회원의 프로필사진 경로를 저장하는 테이블입니다.

file : 서버에 저장된 이미지의  url 경로와 image 이름을 저장합니다.
custom_user : CustomUser 모델을 참조합니다.
"""
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20, null=False)
    active_token = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nickname
    
class ProfileImage(models.Model):
    file = models.ImageField(upload_to="profile/%Y%m%d")
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
