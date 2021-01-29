from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#I added this to set the placeholder in register form
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput



from .models import *


class TalentForm(ModelForm):

	class Meta:
		model = Talent
		fields = '__all__'
		exclude = ['user']
		widgets = {
		'name' : TextInput(attrs={'placeholder':'Enter your name...'}),
		'location' : TextInput(attrs={'placeholder':'Enter your location...'}),
		'website' : TextInput(attrs={'placeholder':'Enter your website...'}),
		'github' : TextInput(attrs={'placeholder':'Enter your github...'}),
		'twitter' : TextInput(attrs={'placeholder':'Enter your twitter...'}),
		'instagram' : TextInput(attrs={'placeholder':'Enter your instagram...'}),
		'phone' : TextInput(attrs={'placeholder':'Enter your celphone number...'}),
		'emailprofile' : TextInput(attrs={'placeholder':'Enter your email...'}),
		'bio' : TextInput(attrs={'placeholder':'A description about your professional background...'}),
		'yearstart' : TextInput(attrs={'placeholder':'Year start...'}),
		'yearend' : TextInput(attrs={'placeholder':'Year end leave in blank if you continue working there...'}),
		'position' : TextInput(attrs={'placeholder':'Enter company position...'}),
		'sideproject' : TextInput(attrs={'placeholder':'Enter your sideproject name...'}),
		'sideproject_website' : TextInput(attrs={'placeholder':'Enter project website URL...'}),

		'current_employment' : TextInput(attrs={'placeholder':'Where are you working? E.g.: IBM, Apple, etc'}),
		'position_employment' : TextInput(attrs={'placeholder':'E.g.: Marketing Analyst, Software developer, etc...'}),
		'yearstart_employment' : TextInput(attrs={'placeholder':'What year did you start?'}),
		'yearend_employment' : TextInput(attrs={'placeholder':'in blank if you continue working here'}),
		'website_employment' : TextInput(attrs={'placeholder':'Enter employment website URL...'}),

		'institution_education' : TextInput(attrs={'placeholder':'Where did you study? E.G: UCLA'}),
		'degree_education' : TextInput(attrs={'placeholder':'What is your major?'}),
		'yearstart_education' : TextInput(attrs={'placeholder':'When did you start estudying'}),
		'yearend_education' : TextInput(attrs={'placeholder':'When did you finish it?'}),
		'website_institution' : TextInput(attrs={'placeholder':'Enter institution website URL...'}),

		'mytalentstory' : TextInput(attrs={'placeholder':'Your awesome story here.'}),
		}
"""
class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
"""



""" OPTION1 but email doesn't work
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



#this help me add placeholders
class CreateUserForm(UserCreationForm):
    username= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Username...'}))
    email= forms.EmailField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email...'}))
    password1= forms.CharField(widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter password...	'}))                               
    password2= forms.CharField(widget= forms.PasswordInput
                           (attrs={'placeholder':'Re-enter password'}))
"""



"""option2 but there's no place holder
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		widgets = {
		'username' : TextInput(attrs={'placeholder':'Username...'}),
		'email' : EmailInput(attrs={'placeholder':'Enter your email...'}),
		'password1' : PasswordInput(attrs={'placeholder':'Enter password..'}),
		'password2' : PasswordInput(attrs={'placeholder':'Re-Enter password..'}),
		}

"""
#Is important to remember that class Meta is to override deffault inputs like username and email
class CreateUserForm(UserCreationForm):
	password1= forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Enter password...	'}))
	password2= forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Re-enter password'}))

	class Meta:
		model = User
		fields = ('username', 'email')
		widgets = {
		'username' : TextInput(attrs={'placeholder':'Username...'}),
		'email' : EmailInput(attrs={'placeholder':'Enter your email...'}),
		}