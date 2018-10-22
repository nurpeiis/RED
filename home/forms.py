from django import forms
from home.models import Post, StageOneInterests, StageOneInterestsPost
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
    NYUAD_resources = StageOneInterests.objects.all()
    user_interests = forms.ModelMultipleChoiceField(queryset=NYUAD_resources)
    other_interests = forms.CharField(widget=forms.Textarea)
    def clean(self):
        cleaned_data = super(NYUADInterestForm, self).clean()
        user_interests = cleaned_data.get('user_interests')
        other_interests = cleaned_data.get('other_interests')
    class Meta:
        model = StageOneInterestsPost
        #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', 'other_interests',)
