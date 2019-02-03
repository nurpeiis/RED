from django.db import models
from accounts.models import User
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from multiselectfield import MultiSelectField
# Create your models here.

#List of things that NYUAD can offer
class BigSection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    imageResource = models.ImageField(upload_to ='image', blank = True )
    class Meta():
        db_table = 'Big Section collection'
        verbose_name_plural = 'Big Sections'
        verbose_name = 'Big Section'

    #it will return the name of the interest whenever StageOneInterests is called
    def __str__(self):
        return (self.name)

#List of choices that user made
class SubSection (models.Model):
    #save the output of the form content under the user database
    section = models.ForeignKey(BigSection, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    steponeimage = models.ImageField(upload_to ='image', blank = True )
    class Meta():
        db_table = 'Sub Section collection'
        verbose_name_plural = 'Sub Sections'
        verbose_name = 'Sub Section'
        ordering = ['section']
    #it will return the name of the interest whenever StageOneInterests is called
    def __str__(self):
        return (self.name)
class Project (models.Model):
    #save the output of the form content under the user database
    section = models.ForeignKey(SubSection, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    imageResource = models.ImageField(upload_to ='image', blank = True )
    class Meta():
        db_table = 'Project collection'
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
    #it will return the name of the interest whenever StageOneInterests is called
    def __str__(self):
        return (self.name)

class StepOneInterest (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_interests = models.ManyToManyField(SubSection, default=None)
    created = models.DateTimeField (auto_now_add = True, blank =True)
    updated = models.DateTimeField (auto_now = True, blank =True)
    def __str__(self):
        return str(self.user)



