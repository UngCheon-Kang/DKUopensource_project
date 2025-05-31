from django.urls import path
from . import views  # 현재 디렉토리의 views 모듈을 import함

app_name = 'detail'  # URL 네임스페이스 설정으로, 다른 앱과 URL 이름 충돌을 방지함

urlpatterns = [
    path('<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),  # 특정 약품의 상세 페이지로 연결됨. 약품 ID를 인자로 받음
    path('<int:medicine_id>/review/', views.add_review, name='add_review'),  # 특정 약품에 대한 리뷰를 추가하는 URL임. 약품 ID를 인자로 받음
]
