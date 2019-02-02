from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm
from home.models import StepOneInterest, SubSection
from django.db.utils import OperationalError
#view for not authorized users:
class HomeNotAuthView(TemplateView):
    template_name = 'home/home.html'
class HomeView(TemplateView):
    template_name = 'home/home.html'

class AboutUsNotAuthView(TemplateView):
    template_name = 'home/aboutus.html'
class AboutUsView(TemplateView):
    template_name = 'home/aboutus.html'
class StepOneView(TemplateView):
    template_name = 'home/RED_form.html'
    def get(self, request):
        #blank if you refresh the page
        form = StepOneInterestForm()
        love = form.fields['user_interests'].queryset
        myList = zip(form, love)
        #'form': form, 'opportunities': opportunities,
        args = {'myList': myList, 'form': form }
        print(args, args['form'].fields['user_interests'].queryset)
        return render(request, self.template_name, args )
    def post(self, request):
        form = StepOneInterestForm(request.POST)
        if form.is_valid():
            obj_form = form.save(commit = False)
            obj_form.user = request.user
            obj_form.save()#save the data in database
            form.save_m2m() # needed since using commit=False
            #clean something like sql injections by code cleaned_data
            return redirect ('home:form')
        return render(request, self.template_name, {'form': form}, )

