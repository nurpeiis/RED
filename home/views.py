from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm, ProjectPostForm
from home.models import StepOneInterest, SubSection, Project, Team
from django.db.utils import OperationalError
from django.http import HttpResponse
from django.contrib import messages
#view for not authorized users:
class HomeNotAuthView(TemplateView):
    template_name = 'home/home.html'
class HomeView(TemplateView):
    template_name = 'home/home.html'
class AboutUsView(TemplateView):
    template_name = 'home/aboutus.html'

class StepOneView(TemplateView):
    template_name = 'home/RED_form.html'
    def get(self, request):
        #blank if you refresh the page
        form = StepOneInterestForm()
        love = form.fields['user_interests'].queryset
        args = {'form': form, 'queryset': love, }
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
def project_view(request, slug=None):
    template_name = "home/project_detail.html"
    instance = get_object_or_404(Project, slug=slug)
    context = {
        "instance":instance,
        "name": instance.name,
    }
    return render(request, template_name, context)


class ProjectPostView(TemplateView):
    template_name = "home/project_post.html"
    def get(self, request):
        form = ProjectPostForm()
        user_list = User.objects.all()
        search_term = ''
        if 'search' in request.GET:
            search_term = request.GET['search']
            user_list = user_list.filter(username__icontains=search_term, first_name__icontains=search_term)#icontains is lowercasing
        context = {'form': form, 'filter': user_list}
        print(user_list)
        return render(request, self.template_name, context)
    def post(self, request):
        form = ProjectPostForm(request.POST)
        if form.is_valid():
            obj_form = form.save(commit = False)
            obj_form.owner = request.user # make the owner the user who created the project
            obj_form.save()#save the data in database
            form.save_m2m() # needed since using commit=False
            #clean something like sql injections by code cleaned_data
            messages.success(request, "Successfully Created Project")
            return redirect ('home:arrange_meeting')
        else:
            messages.error(request, "No success")
        return render(request, self.template_name, {'form': form}, )
#create step 2 view to create new projects. Check following features:
#1. Adding multiple users
#2. Unique Slug
#3. Modify the posts
def project_update(request, slug=None):
    template_name = "home/project_post.html"
    instance = get_object_or_404(Project, slug=slug)
    form = ProjectPostForm(request.POST or None, instance = instance)
    if form.is_valid():
        obj_form = form.save(commit = False)
        obj_form.owner = request.user # make the owner the user who created the project
        obj_form.save()#save the data in database
        form.save_m2m()
        messages.success(request, "Successfully Edited the Project", extra_tags='html_safe')
        return redirect(instance.get_absolute_url())
    context = {
        "instance":instance,
        "name": instance.name,
        "form": form,
    }
    return render(request, template_name, context)
class TeamView(TemplateView):
    template_name = "home/team.html"
    # def team(request):
    #     return HttpResponse('team working')
    def get(self,request):
        queryset = Team.objects.all()
        print(queryset)
        return render(request, self.template_name, {'queryset': queryset})
