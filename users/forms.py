import hashlib
import random

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите почту'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self):
        user = super(UserRegistrationForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1(str(user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
    #         if field_name == 'password1':
    #             field.widget = forms.HiddenInput()
    #
    # def check_pwd(self):
    #     pwd1 = UserProfileForm.cleaned_data.get("password1")  # self.cleaned_data.get("password1")
    #     print(pwd1)
    #     pwd2 = self.get("password2")
    #     print(pwd1, pwd2)
    #     if pwd1 and pwd2 and pwd1 != pwd2:
    #         self.add_error('password1', 'Пароли не совпадают')
    #         print('Пароли не совпадают')
    #     else:
    #         if pwd1:
    #             try:
    #                 password_validation.validate_password(pwd1, self.instance)
    #             except ValidationError as error:
    #                 self.add_error('password2', error)
    #                 print(error)
    #     # return True
    #
    # def save(self):
    #     user = super(UserProfileForm, self).save()
    #     # user.is_active = False
    #     # salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
    #     # user.activation_key = hashlib.sha1(str(user.email + salt).encode('utf8')).hexdigest()
    #     # print(user.password, user.activation_key)
    #     # psw = self.validate_passwords()
    #     print(f'{user.password=}')
    #     # user.set_password(psw)
    #     # user.save()
    #     return user


class UserProfileEditForm(forms.ModelForm):
    # tagline = forms.CharField(label='Тэги',
    #                           widget=forms.TextInput(attrs={'class': 'form-control py-4'}),
    #                           required=False)
    # about_me = forms.CharField(label='О себе',
    #                            widget=forms.TextInput(attrs={'class': 'form-control py-4'}),
    #                            required=False)
    # gender = forms.CharField(label='Пол',
    #                          widget=forms.Select(attrs={'class': 'form-control py-4'}), required=False)

    class Meta:
        model = UserProfile
        fields = ('tagline', 'about_me', 'gender')

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
