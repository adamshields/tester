from django.contrib import admin

# from .models import Environment, Team, Server, 
from .models import Project

# class EnvironmentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     class Meta:
#         model = Environment

# admin.site.register(Environment, EnvironmentAdmin)


# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     class Meta:
#         model = Team

# admin.site.register(Team, TeamAdmin)


# class ServerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     class Meta:
#         model = Server

# admin.site.register(Server, ServerAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)