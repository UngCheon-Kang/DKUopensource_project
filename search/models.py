# search/models.py
from django.db import models

class OTCMedicine(models.Model):
    medicine_name = models.CharField(max_length=255)
    main_ingredients = models.TextField()
    symptom = models.CharField(max_length=255)
    dosage_by_age = models.TextField()
    company = models.CharField(max_length=255)
    precautions = models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.medicine_name

    class Meta:
        managed = False  # Django가 이 테이블을 만들거나 수정하지 않게 함
        db_table = 'otc_medicines'  # 실제 MySQL 테이블 이름
