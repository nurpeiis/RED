from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accounts.models import User
from home.forms import NYUADInterestForm
from home.models import StageOneInterests, StageOneInterestsPost
#view for not authorized users:
class HomeNotAuthView(TemplateView):
    template_name = 'home/home_notauth.html'
class HomeView(TemplateView):
    template_name = 'home/home.html'
class FormView(TemplateView):
    template_name = 'home/RED_form.html'
    def get(self, request):
        #blank if you refresh the page
        form = NYUADInterestForm()
        opportunities = StageOneInterests.objects.all()
        args = {'form': form, 'opportunities': opportunities}
        return render(request, self.template_name, args )
    def post(self, request):
        form = NYUADInterestForm(request.POST)
        if form.is_valid():
            obj_form = form.save(commit = False)
            obj_form.user = request.user
            obj_form .save()#save the data in database
            #clean something like sql injections by code cleaned_data
            form.save_m2m() # needed since using commit=False
            return redirect ('home:form')
        return render(request, self.template_name, {'form': form}, context_instance=RequestContext(request))

