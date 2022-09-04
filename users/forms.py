from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    surname = forms.CharField(max_length=30, required=False, help_text='Отчество')
    phone_number = forms.CharField(max_length=12, required=False, help_text='Номер телефона')

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
