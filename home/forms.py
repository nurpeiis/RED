from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple
from django.db.utils import OperationalError


class StepOneInterestForm(forms.ModelForm):
    #interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=SubSection.objects.all())
    def __init__(self, *args, **kwargs):
        super(StepOneInterestForm, self).__init__(*args, **kwargs)
        self.user_interests = forms.ModelMultipleChoiceField(
            required=True,
            widget=forms.CheckboxSelectMultiple,
            queryset=SubSection.objects.all()
        )
        self.user = None
    class Meta():
        model = StepOneInterest
            #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', )
        widgets = {'sub': forms.CheckboxSelectMultiple}
   
"""   
class SmartGoalsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
"""
