from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection, Project, Membership
from accounts.models import User
from django.forms import CheckboxSelectMultiple
from django.db.utils import OperationalError
from better_filter_widget import BetterFilterWidget
import home.widgets as widgets
from django_select2.forms import Select2MultipleWidget
import django_filters
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
  
class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'subsection', 'members', 'description' ]


