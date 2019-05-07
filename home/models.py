from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django_pglocks import advisory_lock
from django.utils.functional import cached_property
from django.db.models.signals import pre_save
from django.utils.text import slugify
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
class StepOneInterest (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_interests = models.ManyToManyField(SubSection, default=None)
    created = models.DateTimeField (auto_now_add = True, blank =True)
    updated = models.DateTimeField (auto_now = True, blank =True)
    class Meta():
        db_table = 'Step One Interest of User'
        verbose_name_plural = 'Step One Interests of User'
        verbose_name = 'Step One'
        ordering = ["created", "user"]
    def __str__(self):
        return str(self.user)+ " " + str(self.created)

class Team(models.Model):
    name = models.CharField(max_length = 50, unique = True, blank = False)
    title = models.CharField(max_length = 50, blank = False, default='title_default')
    description = models.TextField(blank = False)
    image = models.ImageField(upload_to = 'team_image', blank = True)
    linkedin = models.URLField(blank = True)

class Project(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False,
                                    verbose_name=_("name"))
    slug = models.SlugField(max_length=250, unique=True, null=False, blank=True,
                            verbose_name=_("slug"))
    subsection = models.ManyToManyField(SubSection, default=None, 
                                    verbose_name=_("subsection"))
    description = models.TextField(null=False, blank=False,
                                    verbose_name=_("description"))
    logo = models.FileField(upload_to ='image', blank = True, null=True, verbose_name=_("logo"))
    created_date = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_("created date"))
    modified_date = models.DateTimeField(null=False, blank=False,auto_now=True,
                                         verbose_name=_("modified date"))
    owner = models.ForeignKey(User, null=True, blank=True,
                              related_name="owned_projects", verbose_name=_("owner"), on_delete = models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="projects", 
                                    verbose_name=_("members"))
    total_milestones = models.IntegerField(null=True, blank=True,
                                           verbose_name=_("total milestones"))
    total_story_points = models.FloatField(null=True, blank=True, verbose_name=_("total story points"))
    #Totals
    totals_updated_datetime = models.DateTimeField(null=True, blank=False, auto_now_add=True,
                                                   verbose_name=_("updated date time"), db_index=True)

    total_activity = models.PositiveIntegerField(null=False, blank=False, default=0,
                                                 verbose_name=_("count"),
                                                 db_index=True)

    total_activity_last_week = models.PositiveIntegerField(null=False, blank=False, default=0,
                                                           verbose_name=_("activity last week"),
                                                           db_index=True)

    total_activity_last_month = models.PositiveIntegerField(null=False, blank=False, default=0,
                                                            verbose_name=_("activity last month"),
                                                            db_index=True)

    total_activity_last_year = models.PositiveIntegerField(null=False, blank=False, default=0,
                                                           verbose_name=_("activity last year"),
                                                           db_index=True)

    #_importing = None
    class Meta():
        db_table = 'Project collection'
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
        ordering = ["created_date", "name"]

        

    def __str__(self):
        #return not toople
        template = '{0.name} {0.description}'
        return template.format(self)
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("home:project", kwargs={"slug": self.slug})
    
    def refresh_totals(self, save=True):
        now = timezone.now()
        self.totals_updated_datetime = now
        if save:
            self.save(update_fields=[
                'totals_updated_datetime',
            ])
#https://www.youtube.com/watch?v=Bmvd1O5pNIY
def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Project.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = '{}-{}'.format(slug, qs.first().id)
        #recursive function in a case if slug already exists
        return create_slug(instance, new_slug = new_slug)
    return slug
def pre_save_project_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_project_receiver, sender = Project)
class Membership(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, default=None,
                             related_name="memberships", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=False, blank=False,
                                related_name="memberships", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(null=False, blank=False,
                                        default=timezone.now, verbose_name=_("date joined group"))
    is_admin = models.BooleanField(default=False, null=False, blank=False)
    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"
        unique_together = ("user", "project",)
        ordering = ["project", "user__username"]