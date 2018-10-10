from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
#Manage your backend data.
class UserProfileManager (models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city = 'Abu Dhabi')



class UserProfile(models.Model):
    #passing foreign key, or default model of the user when it registers
    #adding more description to the user
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    description = models.CharField (max_length = 100, default = '')
    city = models.CharField (max_length = 100, default = '')
    website = models.URLField (default= '')
    organization = models.CharField (max_length = 100, default = '')
    phone = models.IntegerField(default = 0)
    #upload_to is specific to file/image upload, because they are large, uploading is optional 
    image = models.ImageField(upload_to = 'profile_image', blank = True)
    london = UserProfileManager()
    #return username in the userprofile page
    def __str__(self):
        return self.user.username
 

def create_profile(sender, **kwargs):
    #if the user has been created then create the User profile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)