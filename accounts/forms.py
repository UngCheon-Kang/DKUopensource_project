from django import forms  # Django의 폼 기능을 사용하기 위해 임포트함
from django.contrib.auth.models import User  # 기본 User 모델을 사용함
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Django의 기본 회원가입, 로그인 폼을 상속받기 위해 임포트함

# 회원가입 폼 정의 클래스임
class SignupForm(UserCreationForm):
    # 이메일 필드를 추가함 (기본 UserCreationForm에는 없음)
    email = forms.EmailField(
        required=True,  # 필수 입력 항목임
        label='이메일',  # 폼에 표시될 레이블 이름
        help_text='유효한 이메일 주소를 입력해주세요.'  # 유저에게 보여줄 안내 문구
    )

    class Meta:  # 내부 설정 클래스임
        model = User  # User 모델을 기반으로 폼을 생성함
        fields = ('username', 'email', 'password1', 'password2')  # 사용할 필드들을 지정함
        labels = {  # 각 필드에 대해 보여줄 레이블을 지정함
            'username': '사용자 이름',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
        }
        help_texts = {  # 각 필드에 대한 도움말을 설정함
            'username': '150자 이하의 영문자, 숫자, @/./+/-/_ 사용 가능',
            'password1': None,  # 기본 비밀번호 도움말 제거
            'password2': None,
        }

    def __init__(self, *args, **kwargs):  # 폼 초기화 시 동작을 커스터마이징함
        super().__init__(*args, **kwargs)
        # 비밀번호1에 대한 커스텀 도움말을 HTML 형식으로 지정함
        self.fields['password1'].help_text = (
            "<ul style='padding-left: 20px; margin: 5px 0;'>"
            "<li>비밀번호는 다른 개인정보와 비슷하지 않아야 합니다.</li>"
            "<li>최소 8자 이상이어야 합니다.</li>"
            "<li>흔히 사용되는 비밀번호는 사용할 수 없습니다.</li>"
            "<li>숫자로만 구성될 수 없습니다.</li>"
            "</ul>"
        )
        # 비밀번호2(확인란)에 대한 도움말 설정
        self.fields['password2'].help_text = "동일한 비밀번호를 한 번 더 입력해주세요."

# 로그인 폼 정의 클래스임
class LoginForm(AuthenticationForm):
    # 사용자명 입력 필드와 라벨을 설정함
    username = forms.CharField(label='아이디')
    # 비밀번호 입력 필드와 라벨을 설정함, 입력 시 * 표시되도록 함
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
