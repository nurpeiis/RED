from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm, ProjectPostForm
from home.models import StepOneInterest, SubSection, Project
from django.db.utils import OperationalError
from django.http import HttpResponse
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
            return redirect ('home:arrange_meeting')
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
class ProjectView(TemplateView):
    template_name = "home/project_detail.html"
class ProjectPostView(TemplateView):
    template_name = "home/project_post.html"
    def get(self, request):
        form = ProjectPostForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = ProjectPostForm(request.POST)
        if form.is_valid():
            obj_form = form.save(commit = False)
            obj_form.owner = request.user # make the owner the user who created the project
            obj_form.save()#save the data in database
            form.save_m2m() # needed since using commit=False
            #clean something like sql injections by code cleaned_data
            return redirect ('home:arrange_meeting')
        return render(request, self.template_name, {'form': form}, )
#create step 2 view to create new projects. Check following features:
#1. Adding multiple users
#2. Unique Slug
#3. Modify the posts
