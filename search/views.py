# search/views.py

from django.shortcuts import render  # 템플릿 렌더링을 위한 함수 import
from .models import OTCMedicine  # 약품 모델 import
import difflib as dl  # 유사도 계산을 위한 difflib 모듈 import

# 초성, 중성, 종성 리스트 정의 (한글 자모 분리를 위해 사용됨)
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 한글을 초성, 중성, 종성으로 분해하는 함수
def decomposed_hangul(korean_word):
    result = []
    for ch in korean_word:
        if '가' <= ch <= '힣':  # 한글 음절인지 확인
            base = ord(ch) - ord('가')  # 유니코드 기준으로 계산
            cho = base // 588  # 초성 인덱스
            jung = (base % 588) // 28  # 중성 인덱스
            jong = base % 28  # 종성 인덱스
            result.extend([CHOSUNG_LIST[cho], JUNGSUNG_LIST[jung], JONGSUNG_LIST[jong]])  # 초중종 분해 후 리스트에 추가
        else:
            result.append(ch)  # 한글이 아니면 그대로 추가
    return result

# 두 문자열 간 유사도를 계산하는 함수 (한글 분해 후 비교)
def calculate_similarity(a, b):
    a_decomposed = decomposed_hangul(a)  # 문자열 a를 분해
    b_decomposed = decomposed_hangul(b)  # 문자열 b를 분해
    return dl.SequenceMatcher(None, a_decomposed, b_decomposed).ratio()  # 유사도 점수 반환 (0.0 ~ 1.0)

# 의약품 검색 처리 함수
def search_medicine(request):
    query = request.GET.get('q', '').strip()  # GET 요청에서 검색어 'q'를 받아오고 양쪽 공백 제거
    best_match = None  # 가장 유사한 약품을 저장할 변수
    highest_score = 0.0  # 최고 유사도 점수 초기화

    if query:
        medicines = OTCMedicine.objects.all()  # 전체 약품 리스트 가져옴
        for med in medicines:
            score = calculate_similarity(query, med.medicine_name)  # 각 약품 이름과 검색어의 유사도 계산
            if score > highest_score:  # 더 높은 유사도일 경우 갱신
                highest_score = score
                best_match = med

        if highest_score < 0.4:  # 유사도가 너무 낮으면 검색 실패로 간주
            best_match = None

    return render(request, 'search/result.html', {'result': best_match})  # 결과를 템플릿에 전달하여 렌더링
