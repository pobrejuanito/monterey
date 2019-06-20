from django import forms
from captcha.fields import CaptchaField
from captcha.fields import CaptchaTextInput

class CustomCaptchaTextInput(CaptchaTextInput):
   template_name = 'captcha_field.html'

class CaptchaContactForm(forms.Form):
   captcha = CaptchaField(widget=CustomCaptchaTextInput(attrs={'id':'contact'}))

class CaptchaAppointmentForm(forms.Form):
   captcha = CaptchaField(widget=CustomCaptchaTextInput(attrs={'id':'appointment'}))   
