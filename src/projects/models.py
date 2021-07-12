from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

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

def pre_save_team(sender, instance, *args, **kwargs):
	slug = slugify(instance.name)
	instance.slug = slug
    
pre_save.connect(pre_save_team, sender=Team)

class ProjectQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)
    
        
class ProjectManager(models.Manager):
    
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def status(self): # This is needed if you want to call something like Product.objects.featured()
        return self.get_queryset().status()

class Project(models.Model):
    PROJECT_STATUS_CHOICES = (
    ('canceled', 'Canceled'),
    ('process', 'Process'),
    ('consultation', 'Consultation'),
    ('testing', 'Lab Testing'),
    ('build', 'Build'),
    ('production', 'Production'),
    ('decommissioning', 'Decommissioning'),
    ('decommissioned', 'Decommissioned'),
    )
    name           = models.CharField(max_length=120, unique=True, verbose_name='Project Name')
    slug           = models.SlugField(blank=True, unique=True)
    status         = models.CharField(max_length=120, default='created', choices=PROJECT_STATUS_CHOICES)
    active         = models.BooleanField(default=True)

    objects = ProjectManager()

    class Meta:
        verbose_name_plural = ('Projects')
        ordering = ['id', 'name']
        db_table = 'projects'

    def __str__(self):
        return self.name

def pre_save_project(sender, instance, *args, **kwargs):
	slug = slugify(instance.name)
	instance.slug = slug

pre_save.connect(pre_save_project, sender=Project)

# class EnvironmentManager(models.Manager):
    
#     def new_or_get(self, request):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()

#         else:
#             cart_obj = Cart.objects.new(user=request.user)
#             new_obj = True
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj

#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated:
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)


# class Environment(models.Model):
#     name           = models.CharField(max_length=300, verbose_name='Project Environment Name')
#     slug           = models.SlugField(unique=True, null=True)
#     project        = models.ForeignKey(Project, verbose_name="Project Name", related_name="project_environment", to_field="name", on_delete=models.CASCADE)

#     objects = EnvironmentManager()

#     class Meta:
#         verbose_name_plural = ('Project Environments')
#         ordering = ['id']
#         db_table = 'project_environments'
    
#     def __str__(self):
#         return self.name


# class Server(models.Model):
#     name           = models.CharField(max_length=200, unique=True, verbose_name='Server Name')
#     slug           = models.SlugField(unique=True, null=True)
    
#     # FOREIGN RELATIONSHIPS
#     teams          = models.ManyToManyField(Team, verbose_name='server_teams', blank=True)
#     project        = models.ForeignKey(Project, verbose_name='server_project', on_delete=models.CASCADE)

    
#     class Meta:
#         verbose_name_plural = ('Servers')
#         ordering = ['id', 'name']
#         db_table = 'servers'

#     def __str__(self):
#         return self.name
