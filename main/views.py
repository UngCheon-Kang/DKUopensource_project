from django.shortcuts import render  # 템플릿 렌더링을 위한 render 함수 import

def home(request):
    return render(request, 'main/home.html')  # 'main/home.html' 템플릿을 렌더링하여 응답으로 반환함
