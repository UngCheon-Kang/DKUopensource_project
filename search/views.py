# search/views.py

from django.shortcuts import render
from .models import OTCMedicine
import difflib as dl

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def decomposed_hangul(korean_word):
    result = []
    for ch in korean_word:
        if '가' <= ch <= '힣':
            base = ord(ch) - ord('가')
            cho = base // 588
            jung = (base % 588) // 28
            jong = base % 28
            result.extend([CHOSUNG_LIST[cho], JUNGSUNG_LIST[jung], JONGSUNG_LIST[jong]])
        else:
            result.append(ch)
    return result

def calculate_similarity(a, b):
    a_decomposed = decomposed_hangul(a)
    b_decomposed = decomposed_hangul(b)
    return dl.SequenceMatcher(None, a_decomposed, b_decomposed).ratio()

def search_medicine(request):
    query = request.GET.get('q', '').strip()
    best_match = None
    highest_score = 0.0

    if query:
        medicines = OTCMedicine.objects.all()
        for med in medicines:
            score = calculate_similarity(query, med.medicine_name)
            if score > highest_score:
                highest_score = score
                best_match = med

        if highest_score < 0.4:
            best_match = None  # 너무 낮으면 결과 없음으로 처리

    return render(request, 'search/result.html', {'result': best_match})
