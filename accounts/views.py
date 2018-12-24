from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
 #customized registration, edit profile forms
from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm #ready template to change form
from django.contrib.auth import update_session_auth_hash # make sure that user is still logged in
#decorator- way of giving edit power
from django.contrib.auth.decorators import login_required
# Create your views here.

#registration page
def register (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            return redirect('/account/register')
    else:
        form = RegistrationForm()
    #take the ready form
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

#login required to view certain pages

#profile page
#primary key is optional 
def view_profile (request, pk=None):
    #to view other people's profile
    #pk = primary key
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render (request, 'accounts/profile.html', args)


#edit your profile
def edit_profile (request):
    #if the user submits changes
    if request.method == 'POST':
        # pass user object so it knows which object it is changing 
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
        else:
            return redirect('/account/profile')
    # if just get
    else:
        form =EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password (request):
    #if the user submits changes
    if request.method == 'POST':
        # pass user object so it knows which object it is changing 
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) #user that tried to change password
            return redirect('/account/profile', {})
        else:
            return redirect('/account/password')
    # if just get
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
