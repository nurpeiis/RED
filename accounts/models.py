from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
# Create your models here.
class Companies(models.Model):
    company_name = models.CharField (max_length=50, unique=True)
    def __str__(self):
        return self.company_name
class User(AbstractUser):
    organization = models.ForeignKey(Companies, on_delete = models.CASCADE, blank = True, null=True, default=1)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    title = models.CharField (max_length=50, blank = True, null=True, default='')
    #upload_to is specific to file/image upload, because they are large, uploading is optional 
    image = models.ImageField(upload_to = 'profile_image', blank = True, null=True)
    #return username in the userprofile page

    def user_model_swapped(**kwargs):
        if kwargs['setting'] == 'AUTH_USER_MODEL':
            apps.clear_cache()
            from myapp import some_module
            some_module.UserModel = get_user_model()
    def __str__(self):
        return self.username
1
