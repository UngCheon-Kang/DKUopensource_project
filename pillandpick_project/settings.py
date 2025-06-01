"""
Django 프로젝트가 어떻게 동작할지를 결정하는 설정 파일
데이터베이스 연결 정보, 설치된 앱 목록, 정적 파일 경로, 템플릿 위치, 인증 관련 설정, 시간대 및 언어 설정 등 다양한 구성 요소를 정의.
덕분에 Django는 각 환경(개발/운영 등)에 맞게 유연하게 동작 가능. 
"""

from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()  # PyMySQL을 MySQLdb로 인식시키기 위해 사용함 (MySQL 연동에 필요함)


# 프로젝트의 루트 경로 설정 (BASE_DIR / 'subdir' 형식으로 경로 지정할 수 있게 해줌)
BASE_DIR = Path(__file__).resolve().parent.parent


# 보안과 관련된 기본 설정
SECRET_KEY = '...'  # Django 프로젝트의 보안 토큰, 배포 시 외부에 공개되지 않도록 주의해야 함
DEBUG = True  # True면 디버깅 모드 (개발 중에는 True, 배포 시에는 False로 설정)
ALLOWED_HOSTS = []  # 배포 시 이 서버로 요청을 허용할 도메인/IP 목록


# 설치된 앱 목록 (Django 기본 앱 + 사용자 정의 앱들)
INSTALLED_APPS = [
    'django.contrib.admin',         # 관리자 페이지 앱
    'django.contrib.auth',          # 인증/권한 관련 기능
    'django.contrib.contenttypes',  # 콘텐츠 타입 시스템
    'django.contrib.sessions',      # 세션 관리
    'django.contrib.messages',      # 메시지 프레임워크
    'django.contrib.staticfiles',   # 정적 파일 관리
    'accounts',     # 사용자 계정 앱
    'search',       # 의약품 검색 기능 앱
    'recommend',    # 증상 기반 추천 기능 앱
    'detail',       # 상세 정보 및 리뷰 기능 앱
    'main',         # 홈화면 및 소개 페이지 앱
]

# 요청 처리 중간에 거치는 미들웨어 설정
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 보안 처리
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 사용자 인증
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 프로젝트의 메인 URL 설정 파일
ROOT_URLCONF = 'pillandpick_project.urls'

# 템플릿 설정 (HTML 렌더링)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 템플릿 엔진
        'DIRS': [BASE_DIR / "templates"],  # 사용자 정의 템플릿 폴더
        'APP_DIRS': True,  # 각 앱의 templates 폴더를 자동으로 검색함
        'OPTIONS': {
            'context_processors': [  # 템플릿에서 사용할 기본 변수들 설정
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# 로그인 성공 후 이동할 기본 페이지
LOGIN_REDIRECT_URL = 'accounts:dashboard'


# 정적 파일 경로 설정 (개발용)
STATIC_URL = '/static/'  # URL 접두어
STATICFILES_DIRS = [BASE_DIR / 'static']  # 실제 정적 파일 위치


# WSGI 애플리케이션 진입점 (배포 시 사용)
WSGI_APPLICATION = 'pillandpick_project.wsgi.application'


# 비밀번호 유효성 검사기 (회원가입 시 보안 강화 목적)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 최소 길이
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 흔한 비번 방지
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 숫자만 비번 방지
    },
]


# 언어, 시간대, 국제화 설정
LANGUAGE_CODE = 'en-us'  # 언어 코드
TIME_ZONE = 'UTC'        # 시간대 (KST로 바꾸려면 'Asia/Seoul' 사용)
USE_I18N = True           # 국제화(i18n) 사용 여부
USE_TZ = True             # 타임존 사용 여부


# 정적 파일 (css, js, 이미지 등) 설정
STATIC_URL = 'static/'


# 기본 PK 필드 타입 설정
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그인하지 않은 사용자가 로그인 필요한 페이지에 접근했을 때 리다이렉트할 URL
LOGIN_URL = 'accounts:login'


# 데이터베이스 설정 (MySQL 연동)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 사용 DB 엔진: MySQL
        'NAME': 'pillandpick_db',              # 데이터베이스 이름
        'USER': 'root',                        # 사용자명
        'PASSWORD': '0000',                    # 비밀번호
        'HOST': '127.0.0.1',                   # 로컬 호스트 주소
        'PORT': '3306',                        # 기본 포트
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # SQL 모드 설정 (정확한 데이터 입력 유도)
        }
    }
}