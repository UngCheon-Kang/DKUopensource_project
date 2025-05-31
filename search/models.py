# search/models.py
from django.db import models  # Django 모델 기능을 사용하기 위한 모듈 import

class OTCMedicine(models.Model):
    medicine_name = models.CharField(max_length=255)  # 약품 이름을 저장하는 문자열 필드
    main_ingredients = models.TextField()  # 주성분 정보를 저장하는 텍스트 필드
    symptom = models.CharField(max_length=255)  # 관련 증상을 저장하는 문자열 필드
    dosage_by_age = models.TextField()  # 연령대별 복용법을 저장하는 텍스트 필드
    company = models.CharField(max_length=255)  # 제조사 정보를 저장하는 문자열 필드
    precautions = models.TextField(null=True, blank=True)  # 주의사항을 저장하는 텍스트 필드 (선택사항)
    image_path = models.CharField(max_length=255, null=True, blank=True)  # 약품 이미지 경로를 저장하는 필드 (선택사항)

    def __str__(self):
        return self.medicine_name  # 객체를 문자열로 표시할 때 약품 이름이 출력되도록 설정함

    class Meta:
        managed = False  # Django가 이 모델에 대응하는 테이블을 생성하거나 수정하지 않도록 설정함 (외부 DB 테이블 사용 시)
        db_table = 'otc_medicines'  # 이 모델이 연결될 실제 데이터베이스 테이블 이름을 명시함
