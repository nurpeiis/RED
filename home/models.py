from django.db import models
from django.conf import settings
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django_pglocks import advisory_lock
from django.utils.functional import cached_property
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
    def __str__(self):
        return str(self.user)+ " " + str(self.created)

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
    created_date = models.DateTimeField(null=False, blank=False,
                                        default=timezone.now, verbose_name=_("created date"))
    modified_date = models.DateTimeField(null=False, blank=False,
                                         verbose_name=_("modified date"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                              related_name="owned_projects", verbose_name=_("owner"), on_delete = models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="projects",
                                     through="Membership", verbose_name=_("members"),
                                     through_fields=("project", "user"))
    total_milestones = models.IntegerField(null=True, blank=True,
                                           verbose_name=_("total milestones"))
    total_story_points = models.FloatField(null=True, blank=True, verbose_name=_("total story points"))
    #Totals
    totals_updated_datetime = models.DateTimeField(null=False, blank=False, auto_now_add=True,
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

    _importing = None

    class Meta():
        db_table = 'Project collection'
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
        ordering = ["name"]
        index_together = [
            ["name"],
        ]

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_date = timezone.now()

        if not self.slug:
            with advisory_lock("project-creation"):
                base_slug = "{}-{}".format(self.owner.username, self.name)
                self.slug = django_slugify(base_slug, self.__class__)
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def refresh_totals(self, save=True):
        now = timezone.now()
        self.totals_updated_datetime = now

        Like = apps.get_model("likes", "Like")
        content_type = apps.get_model("contenttypes", "ContentType").objects.get_for_model(Project)
        qs = Like.objects.filter(content_type=content_type, object_id=self.id)

        self.total_fans = qs.count()

        qs_week = qs.filter(created_date__gte=now - relativedelta(weeks=1))
        self.total_fans_last_week = qs_week.count()

        qs_month = qs.filter(created_date__gte=now - relativedelta(months=1))
        self.total_fans_last_month = qs_month.count()

        qs_year = qs.filter(created_date__gte=now - relativedelta(years=1))
        self.total_fans_last_year = qs_year.count()

        tl_model = apps.get_model("timeline", "Timeline")
        namespace = build_project_namespace(self)

        qs = tl_model.objects.filter(namespace=namespace)
        self.total_activity = qs.count()

        qs_week = qs.filter(created__gte=now - relativedelta(weeks=1))
        self.total_activity_last_week = qs_week.count()

        qs_month = qs.filter(created__gte=now - relativedelta(months=1))
        self.total_activity_last_month = qs_month.count()

        qs_year = qs.filter(created__gte=now - relativedelta(years=1))
        self.total_activity_last_year = qs_year.count()

        if save:
            self.save(update_fields=[
                'totals_updated_datetime',
                'total_fans',
                'total_fans_last_week',
                'total_fans_last_month',
                'total_fans_last_year',
                'total_activity',
                'total_activity_last_week',
                'total_activity_last_month',
                'total_activity_last_year',
            ])

    @cached_property
    def cached_user_stories(self):
        return list(self.user_stories.all())

    @cached_property
    def cached_notify_policies(self):
        return {np.user.id: np for np in self.notify_policies.select_related("user", "project")}

    def cached_notify_policy_for_user(self, user):
        """
        Get notification level for specified project and user.
        """
        policy = self.cached_notify_policies.get(user.id, None)
        if policy is None:
            model_cls = apps.get_model("notifications", "NotifyPolicy")
            policy = model_cls.objects.create(
                project=self,
                user=user,
                notify_level=NotifyLevel.involved)

            del self.cached_notify_policies

        return policy

    @cached_property
    def cached_memberships(self):
        return {m.user.id: m for m in self.memberships.exclude(user__isnull=True)
                                                      .select_related("user", "project", "role")}

    def cached_memberships_for_user(self, user):
        return self.cached_memberships.get(user.id, None)

    def get_roles(self):
        return self.roles.all()

    def get_users(self, with_admin_privileges=None):
        user_model = get_user_model()
        members = self.memberships.all()
        if with_admin_privileges is not None:
            members = members.filter(Q(is_admin=True)|Q(user__id=self.owner.id))
        members = members.values_list("user", flat=True)
        return user_model.objects.filter(id__in=list(members))

    def update_role_points(self, user_stories=None):
        RolePoints = apps.get_model("userstories", "RolePoints")
        Role = apps.get_model("users", "Role")

        # Get all available roles on this project
        roles = self.get_roles().filter(computable=True)
        if roles.count() == 0:
            return

        # Iter over all project user stories and create
        # role point instance for new created roles.
        if user_stories is None:
            user_stories = self.user_stories.all()

        # Get point instance that represent a null/undefined
        # The current model allows duplicate values. Because
        # of it, we should get all poins with None as value
        # and use the first one.
        # In case of that not exists, creates one for avoid
        # unexpected errors.
        none_points = list(self.points.filter(value=None))
        if none_points:
            null_points_value = none_points[0]
        else:
            name = slugify_uniquely_for_queryset("?", self.points.all(), slugfield="name")
            null_points_value = Points.objects.create(name=name, value=None, project=self)

        for us in user_stories:
            usroles = Role.objects.filter(role_points__in=us.role_points.all()).distinct()
            new_roles = roles.exclude(id__in=usroles)
            new_rolepoints = [RolePoints(role=role, user_story=us, points=null_points_value)
                              for role in new_roles]
            RolePoints.objects.bulk_create(new_rolepoints)

        # Now remove rolepoints associated with not existing roles.
        rp_query = RolePoints.objects.filter(user_story__in=self.user_stories.all())
        rp_query = rp_query.exclude(role__id__in=roles.values_list("id", flat=True))
        rp_query.delete()

    @property
    def project(self):
        return self

    def _get_q_watchers(self):
        return Q(notify_policies__project_id=self.id) & ~Q(notify_policies__notify_level=NotifyLevel.none)

    def get_watchers(self):
        return get_user_model().objects.filter(self._get_q_watchers())

    def get_related_people(self):
        related_people_q = Q()

        ## - Owner
        if self.owner_id:
            related_people_q.add(Q(id=self.owner_id), Q.OR)

        ## - Watchers
        related_people_q.add(self._get_q_watchers(), Q.OR)

        ## - Apply filters
        related_people = get_user_model().objects.filter(related_people_q)

        ## - Exclude inactive and system users and remove duplicate
        related_people = related_people.exclude(is_active=False)
        related_people = related_people.exclude(is_system=True)
        related_people = related_people.distinct()
        return related_people

    def add_watcher(self, user, notify_level=NotifyLevel.all):
        notify_policy = create_notify_policy_if_not_exists(self, user)
        set_notify_policy_level(notify_policy, notify_level)

    def remove_watcher(self, user):
        notify_policy = self.cached_notify_policy_for_user(user)
        set_notify_policy_level_to_ignore(notify_policy)

    def delete_related_content(self):
        # NOTE: Remember to update code in taiga.projects.admin.ProjectAdmin.delete_selected
        from taiga.events.apps import (connect_events_signals,
                                       disconnect_events_signals)
        from taiga.projects.epics.apps import (connect_all_epics_signals,
                                             disconnect_all_epics_signals)
        from taiga.projects.tasks.apps import (connect_all_tasks_signals,
                                               disconnect_all_tasks_signals)
        from taiga.projects.userstories.apps import (connect_all_userstories_signals,
                                                     disconnect_all_userstories_signals)
        from taiga.projects.issues.apps import (connect_all_issues_signals,
                                                disconnect_all_issues_signals)
        from taiga.projects.apps import (connect_memberships_signals,
                                         disconnect_memberships_signals)

        disconnect_events_signals()
        disconnect_all_epics_signals()
        disconnect_all_issues_signals()
        disconnect_all_tasks_signals()
        disconnect_all_userstories_signals()
        disconnect_memberships_signals()

        try:
            self.epics.all().delete()
            self.tasks.all().delete()
            self.user_stories.all().delete()
            self.issues.all().delete()
            self.memberships.all().delete()
            self.roles.all().delete()
        finally:
            connect_events_signals()
            connect_all_issues_signals()
            connect_all_tasks_signals()
            connect_all_userstories_signals()
            connect_all_epics_signals()
            connect_memberships_signals()
   

