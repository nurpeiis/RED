from django.urls import include,  path
from home.views import HomeView, FormView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ), #login
    path('form/', FormView.as_view(), name = 'form')
]