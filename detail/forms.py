from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i}점') for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': '후기를 입력하세요'}),
        }
