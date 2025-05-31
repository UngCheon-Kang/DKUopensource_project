from django.urls import path  # URL 경로를 설정하기 위해 path 함수 임포트함
from . import views  # 같은 디렉토리에 있는 views.py 모듈을 임포트함
from django.contrib.auth.views import LogoutView  # 로그아웃 처리를 위한 Django 제공 뷰를 임포트함

app_name = 'accounts'  # URL Reverse 기능을 위한 앱 이름 네임스페이스 지정함

urlpatterns = [
    path('intro/', views.intro, name='intro'),  # 소개 페이지에 대한 URL 라우팅, views.intro 함수와 연결됨
    path('login/', views.login_view, name='login'),  # 로그인 페이지 URL, views.login_view 함수 호출
    path('signup/', views.signup_view, name='signup'),  # 회원가입 페이지 URL, views.signup_view 함수 호출

    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),  
    # Django 내장 LogoutView 사용, 로그아웃 후 'accounts:login'으로 리디렉션함

    path('dashboard/', views.dashboard_view, name='dashboard'),  # 로그인 후 대시보드 페이지로 이동하는 URL
    path('mypage/', views.mypage_view, name='mypage'),  # 마이페이지 URL과 연결됨
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),  
    # 특정 리뷰를 삭제하는 URL, review_id를 매개변수로 받아 views.delete_review 실행
]
