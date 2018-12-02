from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm
from home.models import StepOneInterest, SubSection
from django.db.utils import OperationalError
#view for not authorized users:
class HomeNotAuthView(TemplateView):
    template_name = 'home/home_notauth.html'
class HomeView(TemplateView):
    template_name = 'home/home.html'

class StepOneView(TemplateView):
    template_name = 'home/RED_form.html'
    def get(self, request):
        #blank if you refresh the page
        form = StepOneInterestForm()
        opportunities = SubSection.objects.all()
        l = zip(form, opportunities )
        args = {'form': form, 'opportunities': opportunities, 'l': l}
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

