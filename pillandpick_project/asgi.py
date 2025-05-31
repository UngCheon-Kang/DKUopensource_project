"""
Django에서 실시간 기능을 포함한 비동기(asynchronous) 처리를 지원하기 위해 도입된 설정 파일임. 
웹소켓, 실시간 채팅, 알림 기능처럼 동시다발적인 요청 처리가 필요한 경우에 사용됨
비동기 서버(daphne, uvicorn 등)와 Django 앱을 연결해주는 역할
"""

import os  # 운영체제와 상호작용하기 위한 모듈을 불러옴

from django.core.asgi import get_asgi_application  # Django에서 ASGI application을 생성하는 함수 불러옴

# DJANGO_SETTINGS_MODULE 환경변수를 'pillandpick_project.settings'로 설정함
# 이 설정이 있어야 Django가 어떤 설정 파일을 기준으로 앱을 실행할지 알 수 있음
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pillandpick_project.settings')

# ASGI 서버가 사용할 수 있도록 application 객체를 생성함
# 이는 실제로 서버가 요청을 처리할 때 사용되는 진입점(entry point) 역할을 함
application = get_asgi_application()
