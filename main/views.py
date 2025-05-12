from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  # 템플릿 경로는 이 구조에 맞게 조정
