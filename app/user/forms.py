import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from user.models import User


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Введите адрес эл. почты"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))

    class Meta:
        model = User
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Подтверждение пароля"}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("Пароль слишком короткий. Должно быть как минимум 8 символов.")
        if password.isdigit():
            raise forms.ValidationError("Пароль не должен состоять только из цифр.")
        return password


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return f'uploads/user_images/{filename}'

class UserProfileForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    photo = models.FileField(
        _("Фотография"),
        upload_to=get_file_path
    )
    password = None

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'photo')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['photo'].widget.attrs['class'] = 'custom-file-input'
