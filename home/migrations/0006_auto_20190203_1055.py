# Generated by Django 2.1.3 on 2019-02-03 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181210_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subsection',
            options={'ordering': ['section'], 'verbose_name': 'Sub Section', 'verbose_name_plural': 'Sub Sections'},
        ),
    ]
