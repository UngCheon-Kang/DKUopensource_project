from django.db import models
from django.contrib.auth.models import User
from search.models import OTCMedicine  # 약품 모델 import

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(OTCMedicine, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'medicine')  # 사용자당 1약품에 1개 평가만 가능

    def __str__(self):
        return f"{self.user.username} - {self.medicine.medicine_name} ({self.rating}⭐)"
