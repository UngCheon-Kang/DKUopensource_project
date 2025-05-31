from django.shortcuts import render, redirect  # 템플릿 렌더링 및 URL 리디렉션을 위해 사용함
from django.contrib.auth import authenticate, login, logout  # 인증 및 로그인/로그아웃 기능을 제공하는 모듈 임포트함
from .forms import SignupForm, LoginForm  # 사용자 정의 회원가입 및 로그인 폼 임포트함
from django.contrib.auth.decorators import login_required  # 인증된 사용자만 접근 가능한 뷰에 데코레이터로 사용함
from detail.models import Review  # 리뷰 모델을 detail 앱에서 임포트함
from django.http import HttpResponseForbidden  # 권한 없는 접근에 대한 응답을 위해 사용함
from django.shortcuts import get_object_or_404  # 특정 객체가 없을 경우 404 에러 발생시키기 위해 사용함
from django.contrib import messages  # 사용자에게 메시지를 전달하기 위한 모듈
from django.shortcuts import render, redirect  # 중복이지만 render와 redirect 기능을 다시 가져옴


# 회원가입 뷰 함수
def signup_view(request):
    if request.method == 'POST':  # POST 요청인 경우, 사용자가 회원가입 폼을 제출한 경우임
        form = SignupForm(request.POST)  # 사용자가 입력한 데이터로 폼 객체 생성
        if form.is_valid():  # 폼 유효성 검사
            user = form.save()  # 사용자 정보 저장
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect('accounts:login')  # 로그인 페이지로 리디렉션
    else:
        form = SignupForm()  # GET 요청 시 빈 폼을 생성
    return render(request, 'accounts/signup.html', {'form': form})  # 회원가입 템플릿 렌더링


# 로그인 뷰 함수
def login_view(request):
    if request.method == 'POST':  # POST 요청인 경우 로그인 시도
        form = LoginForm(data=request.POST)  # 로그인 폼에 POST 데이터 전달
        if form.is_valid():  # 폼 유효성 검사
            user = form.get_user()  # 로그인한 사용자 객체 반환
            login(request, user)  # 사용자 로그인 처리
            return redirect('accounts:dashboard')  # 로그인 성공 시 대시보드로 이동
    else:
        form = LoginForm()  # GET 요청이면 빈 폼을 전달
    return render(request, 'accounts/login.html', {'form': form})  # 로그인 템플릿 렌더링


# 로그아웃 처리 함수 (사용되지 않음 — urls.py에서는 Django 제공 LogoutView 사용 중)
def logout_view(request):
    logout(request)  # 사용자 로그아웃 처리
    return redirect('login')  # 로그아웃 후 로그인 페이지로 리디렉션


# 소개 페이지 렌더링
def intro(request):
    return render(request, 'accounts/intro.html')  # 소개 페이지 템플릿 렌더링


# 로그인한 사용자만 접근 가능한 대시보드 페이지
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')  # 대시보드 템플릿 렌더링


# 마이페이지에서 현재 로그인한 사용자의 리뷰 목록 보여줌
@login_required
def mypage_view(request):
    reviews = Review.objects.filter(user=request.user).select_related('medicine')  # 로그인한 사용자의 리뷰 조회
    return render(request, 'accounts/mypage.html', {'reviews': reviews})  # 마이페이지 템플릿에 리뷰 데이터 전달


# 리뷰 삭제 기능, 로그인한 사용자만 가능
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)  # 주어진 ID로 리뷰 객체 조회, 없으면 404 반환

    if review.user != request.user:  # 리뷰 작성자가 현재 로그인한 사용자와 다른 경우
        return HttpResponseForbidden("권한이 없습니다.")  # 403 응답 반환

    review.delete()  # 리뷰 삭제
    messages.success(request, '리뷰가 삭제되었습니다.')  # 삭제 성공 메시지 전달
    return redirect('accounts:mypage')  # 마이페이지로 리디렉션
