from django.urls import path  # URL 패턴을 정의하기 위한 path 함수 import
from . import views  # 현재 디렉토리의 views 모듈을 import

app_name = 'search'  # URL 네임스페이스를 'search'로 지정하여, 다른 앱과의 URL 이름 충돌을 방지함

urlpatterns = [
    path('', views.search_medicine, name='search_medicine'),  # 루트 경로로 접근 시 search_medicine 뷰를 실행하며, URL 이름은 'search_medicine'임
]
