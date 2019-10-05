from django import forms
from django.contrib.auth.models import User
# from users.models import normalUser, stuffUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    years = [i for i in range(1990, 2015)]
    dateOfBirth = forms.DateField(widget=forms.SelectDateWidget(years=years))

    class Meta:
        model = Profile
        fields = ['fullName', 'dateOfBirth', 'address', 'sscRollNo', 'sscRegiNo', 'sscGPA',
                  'hscRollNo', 'hscGPA', 'image']


