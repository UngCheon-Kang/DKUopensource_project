from django.apps import AppConfig  # Django의 App 설정을 위한 기본 클래스 AppConfig를 임포트함

class AccountsConfig(AppConfig):  # 'accounts' 앱의 설정을 정의하는 Config 클래스임
    default_auto_field = 'django.db.models.BigAutoField'  # 기본 자동 증가 필드를 BigAutoField로 설정함
    name = 'accounts'  # 이 설정이 적용되는 앱의 이름을 'accounts'로 지정함
