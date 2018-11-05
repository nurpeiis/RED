from django import forms
from accounts.models import User, Companies #data will be organized consistently
from django.contrib.auth.forms import UserCreationForm # for customized registration
from django.contrib.auth.forms import UserChangeForm #for changing the form
#inherit from class UserCreationForm
class RegistrationForm(UserCreationForm):
    #define anything you want to change
    email = forms.EmailField (required = True)
    organization = forms.ModelChoiceField(queryset=Companies.objects.all())
    title = forms.CharField(required = True)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_messages={'invalid': 'Does not meet requirement'})
    #define the order of fields
    field_order = [ 
            'username', 
            'first_name',
            'last_name',
            'email',
            'organization',
            'title',
            'phone_number',
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
            'organization',
            'title',
            'phone_number',
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
        user.organization = self.cleaned_data['organization']
        user.title = self.cleaned_data['title']
        user.phone_number = self.cleaned_data['phone_number']
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
            'email',
            'organization',
            'title',
            'phone_number'
        ]
    class Meta:
        model = User
        fields = {
            'email', 
            'first_name',
            'last_name',
            'organization',
            'title',
            'phone_number'
        }
    