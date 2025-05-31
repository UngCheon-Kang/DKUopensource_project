from django.shortcuts import render, get_object_or_404, redirect  # 템플릿 렌더링, 객체 불러오기, 페이지 리디렉션을 위한 함수 import
from django.contrib.auth.decorators import login_required  # 로그인한 사용자만 접근 가능하게 하는 데코레이터 import
from django.db import models  # aggregate 함수 사용을 위해 models 모듈 import
from .models import Review  # 현재 앱의 Review 모델 import
from .forms import ReviewForm  # 현재 앱의 ReviewForm 폼 클래스 import
from search.models import OTCMedicine  # 검색 앱의 OTCMedicine 약품 모델 import

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(OTCMedicine, id=medicine_id)  # 약품 ID에 해당하는 객체가 없으면 404 에러 반환
    reviews = Review.objects.filter(medicine=medicine)  # 해당 약품에 대한 모든 리뷰 가져옴
    avg_rating = reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0  # 평균 평점 계산, 없으면 0으로 처리

    context = {
        'medicine': medicine,  # 템플릿에 전달할 약품 객체
        'reviews': reviews,  # 템플릿에 전달할 리뷰 목록
        'avg_rating': round(avg_rating, 1),  # 평균 평점을 소수점 한 자리로 반올림하여 전달
    }
    return render(request, 'detail/medicine_detail.html', context)  # 템플릿 렌더링

@login_required
def add_review(request, medicine_id):
    medicine = get_object_or_404(OTCMedicine, id=medicine_id)  # 약품 ID로 객체 가져오기, 없으면 404
    review = Review.objects.filter(user=request.user, medicine=medicine).first()  # 해당 사용자의 기존 리뷰가 있는지 확인

    if request.method == 'POST':  # 폼 제출 시
        form = ReviewForm(request.POST, instance=review)  # 기존 리뷰가 있으면 수정, 없으면 새로 작성
        if form.is_valid():  # 폼 유효성 검사
            updated = form.save(commit=False)  # 저장 전 사용자 및 약품 정보 추가
            updated.user = request.user
            updated.medicine = medicine
            updated.save()  # 최종 저장
            return redirect('detail:medicine_detail', medicine_id=medicine.id)  # 약품 상세 페이지로 리디렉션
    else:
        form = ReviewForm(instance=review)  # GET 요청 시, 기존 리뷰가 있으면 값 채워서 폼 생성

    return render(request, 'detail/add_review.html', {
        'form': form,  # 템플릿에 전달할 폼 객체
        'medicine': medicine,  # 템플릿에 전달할 약품 정보
        'is_edit': bool(review),  # 기존 리뷰 존재 여부를 템플릿에서 조건문으로 활용
    })
