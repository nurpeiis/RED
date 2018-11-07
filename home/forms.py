from django import forms
from home.models import StageOneInterests, StageOneInterestsPost
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple

class NYUADInterestForm(forms.ModelForm):
    user_interests = TreeNodeMultipleChoiceField(queryset=StageOneInterests.objects.all(), widget=CheckboxSelectMultiple)
    other_interests = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = StageOneInterestsPost
        #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', 'other_interests',)
   
   