from django import forms
from django.forms.fields import MultipleChoiceField
from home.models import StepOneInterest, SubSection
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from django.forms import CheckboxSelectMultiple
from django.db.utils import OperationalError

# From models.py
# class SubSection (models.Model):
#     #save the output of the form content under the user database
#     section = models.ForeignKey(BigSection, on_delete = models.CASCADE)
#     name = models.CharField(max_length=50, unique=True)
#     description = models.TextField()
#     imageResource = models.ImageField(upload_to ='image', blank = True )
#     class Meta():
#         db_table = 'Sub Section collection'
#         verbose_name_plural = 'Sub Sections'
#         verbose_name = 'Sub Section'
#     #it will return the name of the interest whenever StageOneInterests is called
#     def __str__(self):
#         return (self.name)
# class StepOneInterest (models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     user_interests = models.ManyToManyField(SubSection, default=None)
#     created = models.DateTimeField (auto_now_add = True, blank =True)
#     updated = models.DateTimeField (auto_now = True, blank =True)
#     def __str__(self):
#         return str(self.user)

class StepOneInterestForm(forms.ModelForm):
    #interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=SubSection.objects.all())
    def __init__(self, *args, **kwargs):
        super(StepOneInterestForm, self).__init__(*args, **kwargs)
        self.fields['user_interests'].queryset = SubSection.objects.all()
        self.user = None
    class Meta():
        model = StepOneInterest
            #comma should be put at the end so that it will be tuple, if there is one variable to the element
        fields = ('user_interests', )
        widgets = {'sub': forms.CheckboxSelectMultiple}
   

# From views.py
# class StepOneView(TemplateView):
#     template_name = 'home/RED_form.html'
#     def get(self, request):
#         #blank if you refresh the page
#         form = StepOneInterestForm()
#         opportunities = SubSection.objects.all()
#         myList = zip(form, opportunities) 
#         #'form': form, 'opportunities': opportunities,
#         args = {'myList': myList, 'form': form }
#         return render(request, self.template_name, args )
#     def post(self, request):
#         form = StepOneInterestForm(request.POST)
#         print (form)
#         print(form.errors)
#         if form.is_valid():
#             print("hello")
#             obj_form = form.save(commit = False)
#             obj_form.user = request.user
#             obj_form.save()#save the data in database
#             form.save_m2m() # needed since using commit=False
#             #clean something like sql injections by code cleaned_data
#             return redirect ('home:form')
#         return render(request, self.template_name, {'form': form}, )
