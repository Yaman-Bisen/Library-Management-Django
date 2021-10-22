from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django import forms
from .models import BookDetails

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
        labels = {'email':'Email'}


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus':True, 'class':'form-control'}))
    # username = UsernameField(widget=forms.EmailInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class AddBook(forms.Form):
    book_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    author_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
