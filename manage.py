# Django 관리 명령어를 실행하기 위한 유틸리티 스크립트
"""Django's command-line utility for administrative tasks."""  

import os  # 운영 체제 기능을 위한 모듈
import sys  # 시스템 관련 기능을 위한 모듈

def main():
    """Run administrative tasks."""  # Django 관리 명령어를 실행하는 메인 함수
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pillandpick_project.settings')  
    # DJANGO_SETTINGS_MODULE 환경 변수를 'pillandpick_project.settings'로 기본 설정함

    try:
        from django.core.management import execute_from_command_line  # 명령어 실행 함수 import
    except ImportError as exc:
        # Django가 import되지 않으면 예외 발생 및 안내 메시지 출력
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)  # 명령줄 인자를 받아 Django 명령어 실행

if __name__ == '__main__':
    main()  # 이 파일이 직접 실행될 경우 main() 함수 호출
