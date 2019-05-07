from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm
from home.models import StepOneInterest, SubSection, Project, Team
from django.db.utils import OperationalError
from django.http import HttpResponse
from django.contrib import messages
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
        args = {'form': form, }
        return render(request, self.template_name, args )
    def post(self, request):
        form = StepOneInterestForm(request.POST)
        if form.is_valid():
            obj_form = form.save(commit = False)
            obj_form.user = request.user
            obj_form.save()#save the data in database
            form.save_m2m() # needed since using commit=False
            #clean something like sql injections by code cleaned_data
            messages.success(request, "Successfully Submited the First Step Form")
            return redirect ('home:arrange_meeting')
        else:
            messages.error(request, "No success")
        return render(request, self.template_name, {'form': form}, )
class ArrangeMeeting(TemplateView):
    template_name = 'home/arrangemeeting.html'
class StepTwoView(TemplateView):
    template_name = 'home/step_two.html'
    def get(self, request):
        queryset = Project.objects.all()
        context = {
            "object_list":queryset,
            "title": "Experiment"
        }
        return render(request, self.template_name, context)
class TeamView(TemplateView):
    template_name = "home/team.html"
    # def team(request):
    #     return HttpResponse('team working')
    def get(self,request):
        queryset = Team.objects.all()
        print(queryset)
        return render(request, self.template_name, {'queryset': queryset})