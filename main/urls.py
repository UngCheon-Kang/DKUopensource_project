from django.urls import path  # URL 패턴을 정의하기 위한 path 함수 import
from . import views  # 현재 디렉토리의 views 모듈 import

app_name = 'main'  # URL 네임스페이스 설정으로, 템플릿이나 리디렉션 시 'main:home'처럼 사용 가능하게 함

urlpatterns = [
    path('', views.home, name='home'),  # 루트 URL ('/') 요청 시 views.home 뷰를 실행하고 'home'이라는 이름을 부여함
]
