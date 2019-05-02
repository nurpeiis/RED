from rest_framework import viewsets
from home.models import Project
from home.serializers import ProjectListSerializer

class ProjectListViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer