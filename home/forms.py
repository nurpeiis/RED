from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection, Project, Membership, Team
from accounts.models import User
from django.forms import ModelForm, CheckboxSelectMultiple, models
from django.db.utils import OperationalError
from better_filter_widget import BetterFilterWidget
from django_select2.forms import Select2MultipleWidget
import django_filters

from django.contrib.auth.models import User
from django.utils import timezone

#customizing the ModelChoiceField made available in Django
#to have a better control at the data being displayed in the template(s)
class AdvancedModelChoiceIterator(models.ModelChoiceIterator):
    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj), obj)

class AdvancedModelChoiceField(models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return AdvancedModelChoiceIterator(self)
    choices = property(_get_choices,
                       MultipleChoiceField._set_choices)

class StepOneInterestForm(forms.ModelForm):
    user_interests=AdvancedModelChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=SubSection.objects.all(),
        required=True
        )
    user=None

    class Meta():
        model = StepOneInterest
            #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ['user_interests',]
        #widgets = {'sub': forms.CheckboxSelectMultiple}

class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'subsection', 'members', 'description' ]
