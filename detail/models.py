from django.db import models  # Django의 ORM 기능을 제공하는 models 모듈을 import함
from django.contrib.auth.models import User  # Django에서 기본 제공하는 사용자(User) 모델을 import함
from search.models import OTCMedicine  # 약품 모델 import

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 리뷰를 작성한 사용자 정보와 연결함. 사용자 삭제 시 리뷰도 함께 삭제됨
    medicine = models.ForeignKey(OTCMedicine, on_delete=models.CASCADE)  # 리뷰 대상인 약품 정보와 연결함. 약품 삭제 시 리뷰도 함께 삭제됨
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])  # 1~5점 중 하나를 선택하는 별점 필드임
    comment = models.TextField(blank=True)  # 선택적으로 작성 가능한 텍스트 후기 필드임
    created_at = models.DateTimeField(auto_now_add=True)  # 리뷰가 생성된 날짜 및 시간을 자동으로 저장함

    class Meta:
        unique_together = ('user', 'medicine')  # 하나의 사용자(user)가 동일한 약(medicine)에 대해 여러 번 리뷰 작성하지 못하도록 제한함

    def __str__(self):
        return f"{self.user.username} - {self.medicine.medicine_name} ({self.rating}⭐)"  # 관리 페이지 등에 출력될 객체 문자열 표현 정의함
