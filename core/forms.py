from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.forms import TextInput


class MsgForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=TextInput())
    captcha = ReCaptchaField(widget=ReCaptchaV3)
