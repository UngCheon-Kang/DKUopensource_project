from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 회원가입 폼
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='이메일',
        help_text='유효한 이메일 주소를 입력해주세요.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '사용자 이름',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
        }
        help_texts = {
            'username': '150자 이하의 영문자, 숫자, @/./+/-/_ 사용 가능',
            'password1': None,  # 기존 validator 제거
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = (
            "<ul style='padding-left: 20px; margin: 5px 0;'>"
            "<li>비밀번호는 다른 개인정보와 비슷하지 않아야 합니다.</li>"
            "<li>최소 8자 이상이어야 합니다.</li>"
            "<li>흔히 사용되는 비밀번호는 사용할 수 없습니다.</li>"
            "<li>숫자로만 구성될 수 없습니다.</li>"
            "</ul>"
        )
        self.fields['password2'].help_text = "동일한 비밀번호를 한 번 더 입력해주세요."

# 로그인 폼
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
