from django.urls import path
from . import views

app_name = 'detail'

urlpatterns = [
    path('<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('<int:medicine_id>/review/', views.add_review, name='add_review'),
]
