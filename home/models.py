from django.db import models
from accounts.models import User
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from multiselectfield import MultiSelectField
# Create your models here.

#List of things that NYUAD can offer
class StageOneInterests(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    imageResource = models.ImageField(upload_to ='image', blank = True )
    #ForeignKey in this case enables to link the parent with child so used 'self' method
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    class Meta():
        db_table = 'Stage One Interest'
        verbose_name_plural = 'Stage One Interests'
        verbose_name = 'Stage One Interest'

    class MPTTMeta:
        
        order_insertion_by = ['name']
    #it will return the name of the interest whenever StageOneInterests is called
    def __str__(self):
        return (self.name)

#List of choices that user made
class StageOneInterestsPost (models.Model):
    #save the output of the form content under the user database
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_interests = models.ManyToManyField(StageOneInterests)
    created = models.DateTimeField (auto_now_add = True, blank =True)
    updated = models.DateTimeField (auto_now = True, blank =True)


