from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple
from django.db.utils import OperationalError
class StepOneInterestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        steponeinterest_pk = kwargs['steponeinterest_pk']
        del kwargs['steponeitnerest_pk']
        super(StepOneInterestForm, self).__init__(*args, **kwargs)
        choices = [(ts.pk, ts.name) for user_interest in SubSection.objects.filter(pk=steponeinterest_pk)]
        self.fields['user_interests'].choices = choices
    class Meta:
        model = StepOneInterest
            #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', )
        widgets = {'sub': forms.CheckboxSelectMultiple}
   

   
   