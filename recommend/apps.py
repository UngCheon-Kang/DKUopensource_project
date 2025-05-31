from django.apps import AppConfig  # Django 앱의 설정을 정의하는 AppConfig 클래스를 import함

class RecommendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 기본 기본키(auto field)를 BigAutoField로 설정함 (큰 정수형 ID)
    name = 'recommend'  # 이 앱의 이름을 'recommend'로 지정함. Django가 이 앱을 식별할 때 사용됨
