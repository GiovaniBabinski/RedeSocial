from django import forms
from django.contrib.auth.models import User
from .models import Post

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("As senhas não conferem!")

        return cd['password2']


class PostRegistrationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo","descricao")

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo","descricao")
