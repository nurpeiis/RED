from django import forms
from home.models import Post
#ModelForm enables saving the data into databbse from the form
class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder': 'Enter all your interests...'
        }
    ))

    class Meta:

        model = Post
        #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('post',)
