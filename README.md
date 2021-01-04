# Django Oauth Boilerplate
ouath 로그인 구현을 적용한 앱

## 프로젝트 시작하기 

1. 작업 폴더 내에 프로젝트 clone 
```git 
git clone https://github.com/gojaebeom/django_boilerplate.git
```

2. 프로젝트 경로로 이동하여 가상환경 폴더를 만들고 가상환경 구동 (window 기준)
```pip
python -m venv [가상환경명]

venv\Scripts\activate.bat
```

3. 프로젝트에 필요한 의존성 라이브러리 다운로드
```pip
pip install -r requirements.txt
pip install win_mysql_whl/mysqlclient-1.4.6-cp39-cp39-win_amd64.whl
```

4. 프로젝트 기본 경로에 `.env` 파일 생성 및 설정
```python 
DEBUG=on

SECRET_KEY=d6u2p8lspvy-i3r7i*xe&(p=t(u1&me3wm7d$a=53p#t!*ws=2

DATABASE_NAME=[your db name]
DATABASE_USER=[your db user name]
DATABASE_PASSWORD=[your db user password]
DATABASE_HOST=[your domain name or host name]
DATABASE_PORT=[your db port]

EMAIL_HOST_USER=[your email]
EMAIL_HOST_PASSWORD=[your email 2st password]
```

5. 프로젝트 실행시켜보기
```python 
python manage.py runserver
```
