# Generated by Django 2.1.1 on 2018-11-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181105_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
