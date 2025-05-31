from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # 기본 루트 경로: main 앱의 URLConf를 포함함 (예: 홈페이지, 소개 페이지 등)
    path('admin/', admin.site.urls),  # Django 기본 관리자 페이지 경로
    path('accounts/', include('accounts.urls')),  # 사용자 계정 관련 URLConf 포함 (로그인, 회원가입 등)
    path('recommend/', include('recommend.urls', namespace='recommend')),  # 증상 기반 추천 기능 관련 URLConf 포함
    path('search/', include('search.urls')),  # 의약품 검색 기능 URLConf 포함
    path('detail/', include('detail.urls')),  # 의약품 상세 정보 및 리뷰 관련 URLConf 포함
]
