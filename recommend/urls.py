# recommend/urls.py
from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    path('', views.recommend_main, name='symptom_select'),
    path('result/', views.recommend_result, name='recommend_result'),
]
