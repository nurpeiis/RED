from django.urls import include,  path
from home.views import HomeNotAuthView, HomeView, StepOneView, StepTwoView, AboutUsNotAuthView, AboutUsView, ArrangeMeeting, ProjectView, TeamView
from home.views import project_view, ProjectPostView, project_update

app_name = 'home'
urlpatterns = [
    path('not-auth/', HomeNotAuthView.as_view(), name = 'home_notauth'),
    path('', HomeView.as_view(), name = 'home' ), #login
    path('form/', StepOneView.as_view(), name = 'form'),
    path('step-two/', StepTwoView.as_view(), name = 'step_two'),
    path('arrange-meeting/', ArrangeMeeting.as_view(), name = 'arrange_meeting'), 
    path('about-us-notauth/', AboutUsNotAuthView.as_view(), name='about_us_notauth'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
]