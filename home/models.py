from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#save 
class Post (models.Model):
    #save the output of the form content under the user database
    post = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField (auto_now_add = True)
    updated = models.DateTimeField (auto_now = True)