"""RED URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.RED, name='RED')
Class-based views
    1. Add an import:  from other_app.views import RED
    2. Add a URL to urlpatterns:  path('', RED.as_view(), name='RED')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# first hash after the website name
from django.contrib import admin
from django.urls import include, path
from RED import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from home.viewset import ProjectListViewSet, project_detail

router = routers.DefaultRouter()
router.register('projects', ProjectListViewSet)
urlpatterns = [
    path('', views.home_redirect, name = 'home_redirect'), #redirect to home page if just website name is written
    path('admin/', admin.site.urls),
    #namespace give opportunity to use same name in different apps
    path('account/', include('accounts.urls', namespace = 'accounts')), #take the urls from accounts folder
    path('home/', include('home.urls', namespace = 'home')), #take the urls from accounts folder
    path('api/', include(router.urls)),
    path('api/projects/<int:pk>/', project_detail)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

