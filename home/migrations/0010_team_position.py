# Generated by Django 2.1.3 on 2019-05-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_team_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.CharField(default='position_default', max_length=50),
        ),
    ]