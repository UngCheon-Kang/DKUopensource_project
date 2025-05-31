"""
Django의 기본 실행 방식인 동기(synchronous) 환경을 위한 설정 파일임
웹 서버(gunicorn, uWSGI 등)가 Django 프로젝트를 실행할 수 있도록 연결해주는 표준 인터페이스 역할을 함.
"""

import os  # 운영체제와 상호작용을 위한 os 모듈을 불러옴

from django.core.wsgi import get_wsgi_application  # Django의 WSGI 애플리케이션 생성 함수 불러옴

# Django 설정 모듈을 지정함. 프로젝트 실행 시 어떤 설정을 사용할지 정의함
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pillandpick_project.settings')

# WSGI 애플리케이션 객체를 생성하여 서버가 이 객체를 통해 Django 애플리케이션과 통신할 수 있게 함
application = get_wsgi_application()
