from django.urls import include,  path
from home.views import HomeNotAuthView, HomeView, StepOneView

app_name = 'home'
urlpatterns = [
    path('not-auth/', HomeNotAuthView.as_view(), name = 'home_notauth'),
    path('', HomeView.as_view(), name = 'home' ), #login
    path('form/', StepOneView.as_view(), name = 'form')
]