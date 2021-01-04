""" Django settings for config project 🎨"""

""" import HERE 
사용할 외부 라이브러리들을 이곳에 import 시켜주세요.
"""
from pathlib import Path, os # 경로 설정 관련 라이브러리
import environ               # env 설정을 위한 라이브러리 


""" BASE_DIR은 앱의 기본 경로를 가리킵니다. """
BASE_DIR = Path(__file__).resolve().parent.parent


""" Env 
장고 설정 중 보안에 민감한 내용을 .env 파일로 
따로 작성하여 include 시킬 수 있습니다.
env에 작성된 Key 값을 값으로 대입하면 Key에 대한 value 값을 할당합니다.
> env('key name')
"""
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)   
# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


""" SECRET_KEY
보안 주의 : 앱에서 사용될 SECRET_KEY 입니다.
"""
SECRET_KEY = env('SECRET_KEY')


""" DEBUG and ALLOWED_HOSTS setting 
보안 주의 : 앱을 배포할 시 DEBUG를 FALSE로 설정해주세요!
디버깅 모드에서 ALLOWED_HOSTS 변수가 빈 리스트일 경우 ['localhost', '127.0.0.1', '[::1]'] 의미가 됩니다. 즉 로컬 호스트에서만 접근할 수 있습니다.
디버깅 모드를 끄면 일체 접속이 허용되지 않고 하단의 ALLWED_HOSTS 배열에 명시적으로 지정한 호스트에만 접속할 수 있습니다.
"""
DEBUG = True
ALLOWED_HOSTS = []


""" Application definition
장고 앱에서 사용할 응용프로그램을 이곳에서 정의할 수 있습니다.
새로 추가한 앱들을 이곳에 작성해주세요. 
"""
INSTALLED_APPS = [
    # DJANGO DEFAULT INSTALLED APP ⬇
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # <-- AllAuth 사용시 등록해주어야 합니다.
    # ALLAUTH APP HERE ⬇
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    # MY APP HERE ⬇
    'apps.user',
]


""" MIDDLEWARE
미들웨어는 http 요청 or 응답 처리 중간에서 작동하는 시스템입니다.
http 요청이 들어오면 미들웨어를 거쳐서 해당 URL에 등록되어 있는 뷰로 연결해주고, http 응답 역시 미들웨어를 거쳐서 내보냅니다.
"""
MIDDLEWARE = [
    # DJANGO DEFAULT MIDDLEWARE ⬇
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


""" TEMPLATES
장고에서 사용할 템플릿폴더의 기본경로를 설정합니다.
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


""" Database
사용할 데이터베이스를 등록하고 설정할 수 있습니다.
"""
DATABASES = {
    #  SQLLITE 사용시 하단의 주석 풀고 Mysql 설정을 주석처리해주세요.
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },

    # Mysql config
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : env('DATABASE_NAME'),
        'USER'    : env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST'    : env('DATABASE_HOST'),
        'PORT'    : env('DATABASE_PORT'),
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    },
}


""" AUTH_PASSWORD_VALIDATORS
장고가 기본으로 제공하는 비밀번호 유효성 검사 입니다.
사용에 따라 수정이 가능하고 기본적인 기능은 다음과 같습니다.
UserAttributeSimilarityValidator : username(id or email)과 password가 유사한지 채크합니다.
MinimumLengthValidator           : default 8 자와 다른 최소 비밀번호 숫자를 지정합니다.
CommonPasswordValidator          : 넘어온 비밀번호를 common 비밀번호와 비교합니다. 1000개의 common 비밀번호 리스트와 비교 합니다.
NumericPasswordValidator         : 전부 숫자인 비밀번호를 사용하지 못하게 합니다.
"""
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
]


""" TIME SETTING
시간과 관련된 내용을 설정합니다
장고의 TIME_ZONE 기본값은 UTC, USE_TZ 값은 Ture 입니다.

USE_TZ 설정에 따른 차이는 다음과 같습니다.
FALSE : 
장고는 내부적으로 Naive datetime 객체를 사용한다. 
즉 장고 개발 시 Naive datetime 객체를 사용해야 한다. (기준 시간대는 항상 TIME_ZONE)
TRUE  :
장고는 내부적으로 Aware datetime 객체를 사용한다. 
즉 장고 개발 시 Aware datetime 객체를 사용해야 한다. (기준 시간대를 명확히 지정해줘야 함)
"""
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False


""" ROOT_URLCONF
장고의 ROOT_URLCONF 는 config 파일 내의 urls 입니다. 필요에 따라 설정을 바꿀 수 있습니다.
장고 서버로 Http 요청이 들어올 떄마다 URLConf 매핑 List를 처음부터 끝까지 순차적으로 훝으면서 검색합니다.
매칭되는 URL Rule 을 찾지 못할 경우 404 Page Not Found 응답을 발생시킵니다.
"""
ROOT_URLCONF = 'config.urls'


""" WSGI_APPLICATION
WSGI(Web Server Gateway interface)는 
파이썬 스크립트가 웹 서버와 통신하기 위한 인터페이스 규약입니다.
하단의 문장은 wsgi의 위치를 명시하는 설정입니다. 
"""
WSGI_APPLICATION = 'config.wsgi.application'


""" STATIC_URL 설정
javascript , stylesheet, image 등 정적 파일경로에 된련된 부분을 처리합니다. 
하단의 설정에는 media 파일에 대한 설정도 포함되어 있습니다.
* python manage.py collectstatic 명령어를 통해 *
흩어져있는 모든 static 파일들을 한 폴더로 모을 수 있습니다.
"""
# STATIC
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
# ALL STATIC DIR
STATICFILES_DIRS = [
    STATIC_DIR,
    MEDIA_ROOT,
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_file')


""" AUTH and ALLAUTH SETTING
AUTH_USER_MODEL : 장고에서 지원하는 인증모델을 바꿔 사용할 시 해당 모델을 명시해주어야 합니다. 
AUTHENTICATION_BACKENDS : allauth와 장고 username 인증 같이 사용한다는 것을 명시해줍니다.
SITE_ID : django.contrib.sites 앱을 등록시 생기는 테이블의 레코드 번호를 가리킵니다.
LOGIN_REDIRECT_URL : ALLAUTH 로그인 이후에 redirect 할 URL을 작성합니다. 
"""
AUTH_USER_MODEL = 'user.CustomUser'
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/users/create/userinfo'


""" EMAIL 
이메일 인증 시스템에 필요한 정보들을 입력받습니다.
만약 이 기능을 사용하지 않을경우 주석처리해주세요.
"""
EMAIL_HOST = 'smtp.gmail.com' 		               # 메일 호스트 서버
EMAIL_PORT = '587' 			                       # 서버 포트
EMAIL_HOST_USER =  env('EMAIL_HOST_USER')	       # 우리가 사용할 Gmail
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')   # 우리가 사용할 Gmail p
EMAIL_USE_TLS = True			                   # TLS 보안 설정
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER	           # 응답 메일 관련 설정
