
from django import forms
from django.forms import ModelForm, ValidationError
from demo_app.models import BankAccount, AppUser
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from demo_app.models import Article



# class BankAccountForm(forms.Form):
    # name_in_bank = forms.CharField()
    # Account_no = forms.IntegerField()
    # ifsc_code = forms.CharField()
    # Location = forms.CharField()

    # field = ('name_in_bank', 'Account_no', 'ifsc_code')
    #
    # class Meta:
    #     fields = "__all__"

class BankAccountModelForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("username", "email", "password1", "password2",)

class LoginForm(AuthenticationForm):
    pass


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body", "tag")



