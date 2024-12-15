from django import forms
from django.contrib.auth.models import User
from .models import Problems


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)  # commit=False da saqlash, so'ngra o'zgartirish
        user.first_name = self.cleaned_data['first_name']  # first_name ni qo'shish
        user.last_name = self.cleaned_data['last_name']  # last_name ni qo'shish
        user.set_password(self.cleaned_data['password'])  # parolni yangilash
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserProblemForm(forms.Form):
    class Meta:
        model = Problems
        fields = ['firstname', 'lastname', 'email', 'username', 'problem_name', 'problem_description']
