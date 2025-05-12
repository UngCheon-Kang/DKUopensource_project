from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from detail.models import Review
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm

# 회원가입
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 자동 로그인
            return redirect('accounts:login')  # ✅ 네임스페이스 포함해서 수정
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


# 로그인
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('login')

def intro(request):
    return render(request, 'accounts/intro.html')

# accounts/views.py

from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def mypage_view(request):
    reviews = Review.objects.filter(user=request.user).select_related('medicine')
    return render(request, 'accounts/mypage.html', {'reviews': reviews})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # 본인 것만 삭제 가능
    if review.user != request.user:
        return HttpResponseForbidden("권한이 없습니다.")

    review.delete()
    messages.success(request, '리뷰가 삭제되었습니다.')
    return redirect('accounts:mypage')