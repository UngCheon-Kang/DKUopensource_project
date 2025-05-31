# recommend/urls.py
from django.urls import path  # URL 경로를 정의하기 위한 path 함수 import
from . import views  # 현재 디렉토리의 views 모듈 import

app_name = 'recommend'  # URL 네임스페이스를 'recommend'로 지정하여, 템플릿이나 리디렉션에서 'recommend:symptom_select'와 같이 사용 가능하게 함

urlpatterns = [
    path('', views.recommend_main, name='symptom_select'),  # 빈 경로로 접속 시 recommend_main 뷰를 실행, 'symptom_select' 이름 부여
    path('result/', views.recommend_result, name='recommend_result'),  # '/result/' 경로로 접속 시 recommend_result 뷰 실행, 'recommend_result' 이름 부여
]
