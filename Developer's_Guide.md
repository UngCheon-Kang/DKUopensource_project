# ⚙️ Pill and Pick - Developer Guide

이 문서는 Pill and Pick 프로젝트를 실행하고 개발에 참여하기 위한 가이드를 단계별로 제공합니다.

---

##  1단계: GitHub 레포지토리 클론

```bash
git clone https://github.com/your-repo/pillandpick.git
cd pillandpick
```

---

##  2단계: 가상환경(venv) 생성 및 실행

```bash
python -m venv venv
```

### ▶ 가상환경 활성화

* **Windows**:

```bash
venv\Scripts\activate
```

* **macOS / Linux**:

```bash
source venv/bin/activate
```

---

##  3단계: 패키지 설치

```bash
pip install -r requirements.txt
```

---

##  4단계: MySQL 데이터베이스 설정

1. MySQL 접속 후 데이터베이스 생성 및 database 폴더에서 OTC_medicines.sql파일로 테이블 생성 :

```sql
CREATE DATABASE pillandpick_db;
```

2. `pillandpick_project/settings.py` 파일에서 DB 설정 수정:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 사용 DB 엔진: MySQL
        'NAME': 'pillandpick_db',              # 데이터베이스 이름
        'USER': 'root',                        # 사용자명
        'PASSWORD': '0000',                    # 비밀번호
        'HOST': '127.0.0.1',                   # 로컬 호스트 주소
        'PORT': '3306',                        # 기본 포트
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # SQL 모드 설정 (정확한 데이터 입력 유도)
  }
}
```

---

##  5단계: 마이그레이션 적용

```bash
python manage.py makemigrations
python manage.py migrate
```

---

##  6단계: 관리자(superuser) 계정 생성 (선택)

```bash
python manage.py createsuperuser
```

---

##  7단계: 개발 서버 실행

```bash
python manage.py runserver
```

* 접속 주소: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  8단계: 테스트 실행 (선택)

```bash
python manage.py test
```
---

##  문의 

* 문의: `kuc9877@naver.com`






