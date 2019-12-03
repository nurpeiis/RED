from django.urls import include,  path
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeNotAuthView, HomeView, StepOneView, StepTwoView, AboutUsView, ArrangeMeeting, TeamView
# from home.views import project_view, ProjectPostView, project_update
from home.views import ProjectDetailView, ProjectCreateView, ProjectTaskUpdateView, project_update

app_name = 'home'
urlpatterns = [
    path('not-auth/', HomeNotAuthView.as_view(), name = 'home_notauth'),
    path('', HomeView.as_view(), name = 'home' ), #login
    path('form/', StepOneView.as_view(), name = 'form'),
    path('step-two/', StepTwoView.as_view(), name = 'step_two'),
    path('arrange-meeting/', ArrangeMeeting.as_view(), name = 'arrange_meeting'),
    path('about-us-notauth/', AboutUsView.as_view(), name='about_us_notauth'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('team/', TeamView.as_view(), name = 'team'),
    path('team-notauth/', TeamView.as_view(), name = 'team_notauth'),
    # path('project-post/', ProjectPostView.as_view(), name = 'project_post'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name = 'project_detail'),
    # path('project/<slug:slug>/edit', project_update, name = 'project_update' ),
    path('project-post/', ProjectCreateView.as_view(), name = 'project_post'),
    path('project/<slug:slug>/edit', ProjectTaskUpdateView.as_view(), name = 'project_update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
