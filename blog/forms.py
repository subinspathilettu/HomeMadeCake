from django import forms
from .models import Cake
from django.contrib.auth.models import User

class CakeForm(forms.ModelForm):
	class Meta(object):
		model = Cake
		fields = ("title", "price", "image",)

class RegisterForm(forms.ModelForm):
	class Meta(object):
		model = User
		fields = ("username", "email", "password",)
			
						