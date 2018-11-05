from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accounts.models import User

from home.forms import HomeForm, NYUADInterestForm
from home.models import Post, StageOneInterests, StageOneInterestsPost
class HomeView(TemplateView):
    template_name = 'home/home.html'


class FormView(TemplateView):
    template_name = 'home/form_1.html'

    def get(self, request):
        #blank if you refresh the page
        form = HomeForm()
        ## -created = see the latests at the top
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args )
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False) 
            post.user = request.user
            post.save()#save the data in database
            #clean something like sql injections by code cleaned_data
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect ('home:form')
        args = {'form': form, 'text': text}   
        return render(request, self.template_name, args)




class NewFormView(TemplateView):
    template_name = 'home/form_1.html'
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