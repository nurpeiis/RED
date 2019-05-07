from rest_framework import serializers
from home.models import Project
from home.models import SubSection
#List will return all objects
class SubSectiontListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSection
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250,  allow_blank=False,)
    slug = serializers.SlugField(max_length=250, allow_blank=False, )
    subsection = SubSectiontListSerializer(read_only = True, many = True)
    description = serializers.CharField(max_length=250,allow_blank=False)
    class Meta:
        model = Project
        fields = '__all__'

#Non-list view will return only specific projects