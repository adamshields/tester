from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

# GET IN THE HABIT OF THINKING HEY THERE IS SOME ACTION THATS GONNA BE PERFORMED
# What do we want to do with Team
# What do we want to do with Project
# What do we want to do with Environment
# What do we want to do with Server

class Team(models.Model):
    name           = models.CharField(max_length=200, unique=True, verbose_name='Team Name')
    slug           = models.SlugField(unique=True, null=True)
    
    class Meta:
        verbose_name = ('Team')
        verbose_name_plural = ('Teams')
        db_table = 'teams'

    def __str__(self):
        return self.name

class Project(models.Model):
    name           = models.CharField(max_length=120, unique=True, verbose_name='Project Name')
    slug           = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural = ('Projects')
        ordering = ['id', 'name']
        db_table = 'projects'

    def __str__(self):
        return self.name

class Environment(models.Model):
    name           = models.CharField(max_length=300, verbose_name='Project Environment Name')
    slug           = models.SlugField(unique=True, null=True)
    project        = models.ForeignKey(Project, verbose_name="Project Name", related_name="project_environment", to_field="name", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('Project Environments')
        ordering = ['id']
        db_table = 'project_environments'
    
    def __str__(self):
        return self.name


class Server(models.Model):
    name           = models.CharField(max_length=200, unique=True, verbose_name='Server Name')
    slug           = models.SlugField(unique=True, null=True)
    
    # FOREIGN RELATIONSHIPS
    teams          = models.ManyToManyField(Team, verbose_name='server_teams_join', blank=True)
    project        = models.ForeignKey(Project, verbose_name='server_project_join', on_delete=models.CASCADE)

    
    class Meta:
        verbose_name_plural = ('Servers')
        ordering = ['id', 'name']
        db_table = 'servers'

    def __str__(self):
        return self.name

