from django import forms
from .models import Post, Copost
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('name','family', 'date', 'month', 'year', 'img',)
=======
        fields = ('name', 'family', 'date', 'month', 'year', 'img', )

        labels = {
            'name':'이름',
            'family':'카테고리',
            'date':'구매일',
            'month':'',
            'year':'',
            'img':'사진업로드'
        }

        widgets = {
            'name':forms.TextInput(attrs={
                'placeholder':' 무엇을 사셨나요?',
                'size':'20'
            })
        }
>>>>>>> b320db2d0e3841836c050db2fbe6607de48c1e9c


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'password': forms.PasswordInput()}
        help_texts = {
            'username': None,
        }



class CopostForm(forms.ModelForm):
    class Meta:
        model = Copost
        fields = ('cotitle', 'user_name', 'cocontents',)