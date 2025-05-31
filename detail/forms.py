from django import forms  # Django의 폼 기능을 사용하기 위해 forms 모듈을 가져옴
from .models import Review  # 같은 디렉토리에 있는 models.py에서 Review 모델을 가져옴

# 사용자가 작성하는 리뷰 폼을 정의함
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # 이 폼이 사용할 모델을 Review로 지정함
        fields = ['rating', 'comment']  # 폼에 포함될 필드를 평점(rating)과 코멘트(comment)로 설정함
        widgets = {
            # rating 필드는 1점부터 5점까지 선택할 수 있는 드롭다운 메뉴로 표시함
            'rating': forms.Select(choices=[(i, f'{i}점') for i in range(1, 6)]),
            # comment 필드는 3줄짜리 텍스트 영역으로 표시하고, placeholder 문구를 제공함
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': '후기를 입력하세요'}),
        }
