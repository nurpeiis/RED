import re
#automatically assume login_required
from django.conf import settings
from django.urls import reverse #prevent hard coding
from django.shortcuts import redirect
from django.contrib.auth import logout
#include app_name accounts 
app_name = 'accounts'
app_name = 'home'
EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
#ADD INTO LOGIN_EXEMPT_URLS
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware():
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response.
    def process_view(self, request, view_func, view_args, view_kwargs):
        #check that request.user exist
        assert hasattr(request, 'user')
        #lstrip is to remove slash /
        path = request.path_info.lstrip('/')
        
        #redirect user if not authenticated
        #if not request.user.is_authenticated:
         #   print(path)
            #URLS they are trying to look for not in the list redirect
          #  if not any(url.match(path) for url in EXEMPT_URLS):
            #    return redirect(settings.LOGIN_URL)
        #explcitly logout
###
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        
        if path == reverse('accounts:logout').lstrip('/'):
            logout(request)
      
        elif request.user.is_authenticated and url_is_exempt:
            #if user is logged in and wants to go into login or logout page redirect to RED page
            return redirect(settings.LOGIN_REDIRECT_URL)
            
        
        elif request.user.is_authenticated or url_is_exempt:
            return None
            
        else:
            return redirect(settings.LOGIN_URL)
            print(path)
        
