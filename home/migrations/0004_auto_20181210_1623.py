# Generated by Django 2.1.3 on 2018-12-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181210_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='steponeimage',
            field=models.ImageField(blank=True, upload_to='stepone_image'),
        ),
    ]
