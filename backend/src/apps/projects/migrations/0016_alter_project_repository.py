# Generated by Django 4.0.2 on 2022-04-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_project_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.URLField(verbose_name='Link to Repository'),
        ),
    ]