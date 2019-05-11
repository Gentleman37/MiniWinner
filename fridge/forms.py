from django import forms
from .models import Post, Copost
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'family', 'date', 'month', 'year', 'img', )


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
        fields = ('cotitle', 'cocontents',)