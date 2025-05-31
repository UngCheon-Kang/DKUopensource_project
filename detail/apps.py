from django.apps import AppConfig  # Django 애플리케이션 설정을 위한 AppConfig 클래스를 가져옴


# 'detail' 앱의 설정을 정의하는 클래스임
class DetailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 기본 자동 생성 필드 타입을 BigAutoField로 지정함
    name = 'detail'  # 이 설정 클래스가 적용될 앱의 이름을 'detail'로 지정함
