
# recommend/views.py
from search.models import OTCMedicine  # 약품 테이블 import
from django.shortcuts import render, redirect
from django.db import models



def recommend_main(request):
    return render(request, 'recommend/symptom_select.html') 


def recommend_result(request):
    if request.method == 'POST':
        selected_symptoms = request.POST.getlist('symptoms')
        if selected_symptoms:
            # 증상 리스트 중 하나라도 포함된 약만 필터링 (OR 조건)
            query = models.Q()
            for symptom in selected_symptoms:
                query |= models.Q(symptom__icontains=symptom)
            medicines = OTCMedicine.objects.filter(query).distinct()
        else:
            medicines = []
        return render(request, 'recommend/recommend_result.html', {
            'selected_symptoms': selected_symptoms,
            'medicines': medicines,
        })
    return redirect('recommend:symptom_select')
