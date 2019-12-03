from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from accounts.models import User
from home.forms import StepOneInterestForm, ProjectPostForm
from home.models import StepOneInterest, SubSection, Project, Team
from django.db.utils import OperationalError
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic

from django.forms.models import inlineformset_factory
# from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import (
    CreateView, DetailView, FormView, ListView, TemplateView
)
from home.forms import ProjectTaskFormset
from django.urls import reverse



#view for not authorized users:
class HomeNotAuthView(TemplateView):
    template_name = 'home/home.html'
class HomeView(TemplateView):
    template_name = 'home/home.html'
class AboutUsView(TemplateView):
    template_name = 'home/aboutus.html'
class TeamView(TemplateView):
    template_name = "home/team.html"
    def get(self,request):
        queryset = Team.objects.all()
        print(queryset)
        return render(request, self.template_name, {'queryset': queryset})

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

class ProjectDetailView(TemplateView):
    template_name = "home/project_detail.html"
    def get(self,request,slug):
        instance = get_object_or_404(Project, slug=slug)
        context = {
            "instance":instance,
            "name": instance.name,
        }
        return render(request, self.template_name, context)


## FROM DJANGO-NESTED-INLINE-FORMSETS-EXAMPLE
# class ProjectCreateView(CreateView):
#     """
#     Only for creating a new project. Adding tasks to it is done in the
#     ProjectTaskUpdateView().
#     """
#     model = Project
#     template_name = 'home/project_post.html'
#     fields = ["name","subsection","owner","description","members","SMARTgoals"]
#
#     def form_valid(self, form):
#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'The project was added.'
#         )
#         return super().form_valid(form)
#
#
# class ProjectTaskUpdateView(SingleObjectMixin, FormView):
#     """
#     For adding tasks to a Project, or editing them.
#     """
#
#     model = Project
#     template_name = 'home/project_post.html'
#
#     def get(self, request, *args, **kwargs):
#         # The Project we're editing:
#         self.object = self.get_object(queryset=Project.objects.all())
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         # The Project we're uploading for:
#         self.object = self.get_object(queryset=Project.objects.all())
#         return super().post(request, *args, **kwargs)
#
#     def get_form(self, form_class=None):
#         """
#         Use our formset, and pass in the Project object.
#         """
#         return ProjectTaskFormset(**self.get_form_kwargs(), instance=self.object)
#
#     def form_valid(self, form):
#         """
#         If the form is valid, redirect to the supplied URL.
#         """
#         form.save()
#
#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'Changes were saved.'
#         )
#
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse('home:project')





# ##fROM SWAPP
class ProjectCreateView(CreateView):
    template_name = "home/project_post.html"
    model = Project
    fields = ["name","subsection","owner","description","members","SMARTgoals","tasks","taskDue"]

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["tasks"] = ProjectTaskFormset(self.request.POST)
        else:
            data["tasks"] = ProjectTaskFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        tasks = context["tasks"]
        self.object = form.save()
        if tasks.is_valid():
            tasks.instance = self.object
            tasks.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home:project_detail')

class ProjectTaskUpdateView(UpdateView):
    model = Project
    template_name = 'home/project_post.html'
    fields = ["name","subsection","owner","description","members","SMARTgoals"]

#     def get(self, request):
#         form = ProjectPostForm()
#         user_list = User.objects.all()
#         search_term = ''
#         if 'search' in request.GET:
#             search_term = request.GET['search']
#             user_list = user_list.filter(username__icontains=search_term, first_name__icontains=search_term)#icontains is lowercasing
#         context = {'form': form, 'filter': user_list}
#         print(user_list)
#         return render(request, self.template_name, context)

    # def get(self, request):
    #     form = ProjectPostForm()
    #     user_list = User.objects.all()
    #     context = {
    #         'form' : form,
    #         'tasks' : ProjectTaskFormset(self.request.POST, instance=self.object)
    #     }
    #     return render(request,self.template_name,context)
    # def post(self, request):
    #         form = ProjectPostForm(request.POST)
    #         if form.is_valid():
    #             obj_form = form.save(commit = False)
    #             obj_form.owner = request.user # make the owner the user who created the project
    #             obj_form.save()#save the data in database
    #             form.save_m2m() # needed since using commit=False
    #             #clean something like sql injections by code cleaned_data
    #             messages.success(request, "Successfully Created Project")
    #             return redirect ('home:project')
    #         else:
    #             messages.error(request, "No success")
    #         return render(request, self.template_name, {'form': form}, )
    #
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data to make sure that our formset is rendered.
        # the difference with CreateView is that on this view we pass instance argument
        # to the formset because we already have the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["tasks"] = ProjectTaskFormset(self.request.POST, instance=self.object)
        else:
            data["tasks"] = ProjectTaskFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        tasks = context["tasks"]
        self.object = form.save()
        if tasks.is_valid():
            tasks.instance = self.object
            tasks.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home:project_detail')












# class ProjectPostView(TemplateView):
#     template_name = "home/project_post.html"
#     def get(self, request):
#         form = ProjectPostForm()
#         user_list = User.objects.all()
#         search_term = ''
#         if 'search' in request.GET:
#             search_term = request.GET['search']
#             user_list = user_list.filter(username__icontains=search_term, first_name__icontains=search_term)#icontains is lowercasing
#         context = {'form': form, 'filter': user_list}
#         print(user_list)
#         return render(request, self.template_name, context)
#     def post(self, request):
#         form = ProjectPostForm(request.POST)
#         if form.is_valid():
#             obj_form = form.save(commit = False)
#             obj_form.owner = request.user # make the owner the user who created the project
#             obj_form.save()#save the data in database
#             form.save_m2m() # needed since using commit=False
#             #clean something like sql injections by code cleaned_data
#             messages.success(request, "Successfully Created Project")
#             return redirect ('home:arrange_meeting')
#         else:
#             messages.error(request, "No success")
#         return render(request, self.template_name, {'form': form}, )
#
# #create step 2 view to create new projects. Check following features:
# #1. Adding multiple users
# #2. Unique Slug
# #3. Modify the posts
def project_update(request, slug=None):
    template_name = "home/project_post.html"
    instance = get_object_or_404(Project, slug=slug)
    form = ProjectTaskFormset(request.POST or None, instance = instance)
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
