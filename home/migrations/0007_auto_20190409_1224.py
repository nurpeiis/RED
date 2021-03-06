# Generated by Django 2.1.3 on 2019-04-09 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20190203_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined group')),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
                'ordering': ['project', 'user__username'],
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_date', 'name'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='steponeinterest',
            options={'ordering': ['created', 'user'], 'verbose_name': 'Step One', 'verbose_name_plural': 'Step One Interests of User'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='imageResource',
        ),
        migrations.RemoveField(
            model_name='project',
            name='section',
        ),
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='image', verbose_name='logo'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='members'),
        ),
        migrations.AddField(
            model_name='project',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified date'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='project',
            name='subsection',
            field=models.ManyToManyField(default=None, to='home.SubSection', verbose_name='subsection'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_activity',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='count'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_activity_last_month',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='activity last month'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_activity_last_week',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='activity last week'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_activity_last_year',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='activity last year'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_milestones',
            field=models.IntegerField(blank=True, null=True, verbose_name='total milestones'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_story_points',
            field=models.FloatField(blank=True, null=True, verbose_name='total story points'),
        ),
        migrations.AddField(
            model_name='project',
            name='totals_updated_datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='updated date time'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=250, verbose_name='name'),
        ),
        migrations.AlterModelTable(
            name='steponeinterest',
            table='Step One Interest of User',
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='home.Project'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('user', 'project')},
        ),
    ]
