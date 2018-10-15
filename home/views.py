from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm
from home.models import Post 
class HomeView(TemplateView):
    template_name = 'home/home.html'


class FormView(TemplateView):
    template_name = 'home/form.html'

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