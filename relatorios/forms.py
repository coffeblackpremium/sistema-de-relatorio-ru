from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from psutil import users
from traitlets import default
from .choices_coord import LISTA_COORDENACAO

#Entrar no site para ter como exemplo: https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields


class RegisterEmployee(UserCreationForm):
    username = forms.CharField(help_text="Necessário ter um Usuario para ser seu login", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um usuario para acessar sua conta'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}), max_length=32, help_text='Digite o seu Primeiro nome')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Sobrenome')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Entre com um Endereço Válido')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha novamente'}))
    sector_name = forms.ChoiceField(
        required=True,
        choices=LISTA_COORDENACAO,
    )
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super(RegisterEmployee, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.sector_name = self.cleaned_data['sector_name']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterEmployee, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-1'