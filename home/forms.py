from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple
from django.db.utils import OperationalError
class StepOneInterestForm(forms.ModelForm):
    user_interests_StepOne = forms.ModelMultipleChoiceField(queryset=SubSection.objects.all(), widget=CheckboxSelectMultiple)
    class Meta:
        model = StepOneInterest
            #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', )
   

   
   