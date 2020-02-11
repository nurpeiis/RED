# Generated by Django 2.1.3 on 2019-12-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_project_smartgoals'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='taskDue',
            field=models.DateTimeField(blank=True, null=True, verbose_name='duedate for each tasks'),
        ),
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.TextField(blank=True, null=True, verbose_name='tasks'),
        ),
    ]