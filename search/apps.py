from django.apps import AppConfig  # Django 앱 설정을 위한 AppConfig 클래스 import

class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 모델에서 기본으로 사용할 자동 증가 필드 타입을 BigAutoField로 설정함
    name = 'search'  # 이 앱의 이름을 'search'로 지정함. 프로젝트 내에서 앱을 식별하는 데 사용됨
