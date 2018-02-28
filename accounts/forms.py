from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','email','password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '아이디',
            'email': '이메일',
            'password': '패스워드'
        }
    
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15