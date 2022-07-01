from dataclasses import fields
from pickle import LIST
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, ModelForm

from relatorios.models import TableActionModel, TableEventModel, User
from .choices_coordenacao import LISTA_COORDENACAO



#Crianndo um Formulario para Registro
class RegisterEmployee(UserCreationForm):
    username = forms.CharField(help_text="Necessário ter um Usuario para ser seu login", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um usuario para acessar sua conta'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}), max_length=32, help_text='Digite o seu Primeiro nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}), max_length=32, help_text='Sobrenome')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Entre com um Endereço Válido')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha novamente'}))
    sector_name = forms.ChoiceField(
        choices=LISTA_COORDENACAO,  
    )
    #Usando o Models User do 'relatorios/models'
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('sector_name','first_name', 'last_name', 'email',)
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.sector_name = self.cleaned_data['sector_name']
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterEmployee, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-1'

class TableActionForm(ModelForm):
    class Meta:
        model = TableActionModel
        fields = ['acao_realizada', 'tecnico_presencial', 'tecnico_nao_presencial',
        'outras_acoes', 'numbers_employee', 'description_action', 'date_actions']


class TableEventForm(ModelForm):
    class Meta:
        model = TableEventModel
        fields = ['title_event', 'event_feature', 'date_initial', 'date_final']
        widgets = {
            'title_event': forms.TextInput(),
            'date_initial': forms.DateInput(attrs={'type':'date'}),
            'date_final': forms.DateInput(attrs={'type':'date'})
        }

    def clean(self):
        super(TableEventForm, self).clean()

        title_event = self.cleaned_data.get("title_event")
        event_feature = self.cleaned_data.get("event_feature")
        date_initial = self.cleaned_data.get("date_initial")
        date_final = self.cleaned_data.get("date_final")

        return self.cleaned_data


    def __init__(self, *args, **kwargs):
        super(TableEventForm, self).__init__(*args, **kwargs)
        self.fields['event_feature'].label = "Característica do Evento"