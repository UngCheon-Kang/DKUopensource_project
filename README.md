# 💊 Pill and Pick

**Pill and Pick**은 의약품 정보를 검색하고, 증상 기반으로 약품을 추천하며, 사용자 리뷰(별점 및 코멘트)를 통해 보다 신뢰도 높은 약품 선택을 지원하는 웹 기반 커뮤니티 서비스입니다.

---

## 주요 기능

* **의약품명 검색**: 유사도 알고리즘을 활용하여 오타에도 유연하게 대응하는 약품명 검색
* **증상 기반 추천**: 체크박스로 복수 증상 선택 후 해당 약품 추천
* **사용자 리뷰**: 로그인한 사용자가 별점(1\~5점)과 코멘트를 남길 수 있음
* **로그인/회원가입**: Django 기본 auth를 사용한 인증 시스템

---

## 사용 기술

| 분야     | 기술 스택                         |
| ------ | ----------------------------- |
| 백엔드    | Django 4.x, Python 3.10       |
| 프론트엔드  | HTML, JS, CSS |
| 데이터베이스 | MySQL 8.x                     |
| 기타     | GitHub, venv, difflib         |

---

## 실행 방법

1. 레포지토리 클론

```bash
git clone https://github.com/your-repo/pillandpick.git
cd pillandpick
```

2. 가상환경 설정

```bash
python -m venv venv
source venv/bin/activate        # Windows는 venv\Scripts\activate
```

3. 패키지 설치

```bash
pip install -r requirements.txt
```

4. MySQL 데이터베이스 설정 및 OTC_medici성

```bash
CREATE DATABASE pillandpick;
```

5. `settings.py`에서 DB 설정값 변경 후 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

6. 개발 서버 실행

```bash
python manage.py runserver
```
---

## 문의

* 이메일: [kuc9877@naver.com](mailto:kuc9877@naver.com)

