from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'accounts'

urlpatterns = [
    path('intro/', views.intro, name='intro'),  # 소개 페이지 라우트 추가
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
