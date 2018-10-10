from django import forms
from django.contrib.auth.models import User #data will be organized consistently
from django.contrib.auth.forms import UserCreationForm # for customized registration
from django.contrib.auth.forms import UserChangeForm #for changing the form
#inherit from class UserCreationForm
class RegistrationForm(UserCreationForm):
    #define anything you want to change
    email = forms.EmailField (required = True)
    #define the order of fields
    field_order = [ 
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
    #Meta data - if photo resolution and pixels is meta data
    class Meta:
        model = User
        #fields that we want to see
        fields = {
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }
       
        
    #function to save the data
    def save (self, commit = True):
        #wait until you did not do name, email and others
        user = super (RegistrationForm, self). save(commit=False)
        #no code in the field = no hacking
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return User

class EditProfileForm (UserChangeForm):
    #fields = fields that we want to include
    #exlude = fields that we want to exclude
     #define the order of fields
    field_order = [ 
            'first_name',
            'last_name',
            'email'
        ]
    class Meta:
        model = User
        fields = {
            'email', 
            'first_name',
            'last_name',
            'password'
        }
