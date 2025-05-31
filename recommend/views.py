# recommend/views.py
from search.models import OTCMedicine  # 약품 테이블 import
from django.shortcuts import render, redirect  # 템플릿 렌더링과 리디렉션을 위한 함수 import
from django.db import models  # Q 객체 사용을 위해 models 모듈 import


def recommend_main(request):
    return render(request, 'recommend/symptom_select.html')  # 증상 선택 페이지를 렌더링함


def recommend_result(request):
    if request.method == 'POST':  # 사용자가 증상 선택 후 폼을 제출한 경우
        selected_symptoms = request.POST.getlist('symptoms')  # 선택된 증상들을 리스트 형태로 가져옴
        if selected_symptoms:
            # 선택된 증상들 중 하나라도 포함된 약품을 찾기 위한 Q 객체 구성 (OR 조건)
            query = models.Q()
            for symptom in selected_symptoms:
                query |= models.Q(symptom__icontains=symptom)  # symptom 필드에 각 증상이 포함되는지 조건 추가
            medicines = OTCMedicine.objects.filter(query).distinct()  # 중복 제거 후 조건에 맞는 약품 리스트 조회
        else:
            medicines = []  # 증상이 선택되지 않았을 경우 빈 리스트 반환
        return render(request, 'recommend/recommend_result.html', {
            'selected_symptoms': selected_symptoms,  # 템플릿에 선택한 증상 전달
            'medicines': medicines,  # 템플릿에 추천된 약품 리스트 전달
        })
    return redirect('recommend:symptom_select')  # POST 요청이 아닌 경우 증상 선택 페이지로 리디렉션
