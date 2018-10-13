from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from home.forms import HomeForm
#from home.models import Post 
class HomeView(TemplateView):
    template_name = 'home/home.html'


class FormView(TemplateView):
    template_name = 'home/form.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            #clean something like sql injections by code cleaned_data
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect ('home:form')
        args = {'form': form, 'text': text}   
        return render(request, self.template_name, args)