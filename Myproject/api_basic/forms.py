from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegristrationForm(UserCreationForm):
    Email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# BIRTH_YEAR_CHOICE = ['2000', '2001', '2002', '2003', '2004']




# class CustomerForm(forms.Form):
#     firstName = forms.CharField(max_length=100, required=True)
#     lastName = forms.CharField(max_length=100)
#     Email = forms.EmailField(max_length=100)
#     password = forms.PasswordInput
#     Address = forms.CharField(widget=forms.Textarea)
#     Age = forms.PositiveIntegerField(max_length=50)
#     DateOfBirth = forms.DateField(label='DOB', widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))
