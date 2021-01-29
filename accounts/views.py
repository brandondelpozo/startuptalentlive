from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from taggit.models import Tag

from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

# Create your views here.
from .models import *
from .forms import CreateUserForm, TalentForm #I named the 'CustomerForm' as 'TalentForm'
from .decorators import unauthenticated_user, allowed_users 

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='talent')
			user.groups.add(group)
			Talent.objects.create(
				user=user,  #the way how a user could change his username 'user' is the same as emailprofile
				name=user.username,
				emailprofile=user.email #this emailprofile get info from UserCreationForm - email #I have to fix this later
				)

			messages.success(request, 'Account was created for ' + username)
			
			return redirect('login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def home(request):
	return render(request, 'accounts/home.html')

def profilePage(request): #This show kyle mckiou profile, probably I won't use it later
	context = {}
	return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['talent', 'admin'])
def editprofilePage(request):
	talent = request.user.talent
	form = TalentForm(instance=talent)
	
	if request.method == 'POST':
		form = TalentForm(request.POST, request.FILES,instance=talent)
		if form.is_valid():
			form.save()

			
	context = {'form':form}
	return render(request, 'accounts/editprofile.html', context) #this show a editable profile without custom URL only startuptalents.com/editableprofile

#def profiletest(request, pk_test):   #this show startuptalents.com/prifletest/userid #E.G. this show startuptalents.com/prifiletest/5
#	talent = Talent.objects.get(id=pk_test)
#
#	context = {'talent':talent}
#	return render(request, 'accounts/profiletest.html', context)

def publicprofile(request, username): 
	user = get_object_or_404(User, username=username) #MyModel.objects.get(username=username) if doesn't exist show http404
	return render(request, 'accounts/publicprofile.html', {'profile': user})


#I'm here :D


#def talent(request):
#	return HttpResponse('talent') #in blank

#def recruiter(request):
#	return HttpResponse('recruiter') #in blank