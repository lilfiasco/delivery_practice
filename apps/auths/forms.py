import re
from datetime import timedelta,datetime

#Django
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.forms import AuthenticationForm

#Local
from .models import CustomUser, Coworker, Franchise


class CustomUserForm(forms.ModelForm):
    phone_number = forms.CharField(
        label='Номер телефона',
        min_length=12,
        max_length=12,
        widget=forms.TextInput(attrs={'id': 'phone-number-input'})
    )
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')
    first_name = forms.CharField(min_length=2,max_length=69,
        validators=[
            RegexValidator(
                regex=r'^[\w\'\-,.А-Яа-я][^\d_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$',
                message="Имя должно состоять не менее чем из 3 символов и не должно содержать цифр или специальных символов."
            )
        ],
        
        label='Имя'
    )
    last_name = forms.CharField(min_length=2,max_length=69,
        validators=[
            RegexValidator(
                regex=r'^[\w\'\-,.А-Яа-я][^\d_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$',
                message="Фамилия должна состоять не менее чем из 3 символов и не должна содержать цифр или специальных символов."
            )
        ],
        
        label='Фамилия'
    )
    birth_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Birth Date', 'class': 'form-control', 'type': 'date'}),
        label='День рождения'
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'birth_date',)

    def clean(self):
        cleaned_data = super().clean()

        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if first_name:
            if re.search(r'[\d_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]', first_name):
                self.add_error('first_name', 'Недопустимый формат данных')

        if last_name:
            if re.search(r'[\d_!¡?÷?¿\/\\+=@#$%ˆ&*(){}|~<>;:[\]]', last_name):
                self.add_error('last_name', 'Недопустимый формат данных')

        if not password:
            self.add_error('password', 'Это поле не может быть пустым')

        if password and password2 and password != password2:
            self.add_error('password2', 'Пароли не совпадают')

        return cleaned_data

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 16:
            raise ValidationError("Доступ запрещен! Вам должно быть не менее 16 лет.")

        return birth_date


class CoworkerForm(CustomUserForm):    
    franchise = forms.ModelChoiceField(
        queryset=Franchise.objects.all(),
        label='Франшиза'
    )
    class Meta(CustomUserForm.Meta):
        model = Coworker
        fields = CustomUserForm.Meta.fields + ('franchise',)

        