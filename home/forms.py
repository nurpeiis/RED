from django import forms
from home.models import Post, StageOneInterests, StageOneInterestsPost
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple
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

class NYUADInterestForm(forms.ModelForm):
    user_interests = TreeNodeMultipleChoiceField(queryset=StageOneInterests.objects.all(), widget=CheckboxSelectMultiple)
    other_interests = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = StageOneInterestsPost
        #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', 'other_interests',)
   
   