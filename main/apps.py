from django.apps import AppConfig  # Django 앱 구성 설정을 위한 AppConfig 클래스 import

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 기본 자동 필드 타입을 BigAutoField로 설정함 (자동 증가 정수형 ID)
    name = 'main'  # 이 앱의 전체 Python 경로 또는 이름을 지정함. 프로젝트에서 'main'이라는 앱으로 인식됨
