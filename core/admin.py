from django.contrib import admin
from .models import About, Client, Service, Project, Message, Team

admin.site.register(About)
admin.site.register(Client)
admin.site.register(Service)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_name", "slug"]
    prepopulated_fields = {"slug": ("project_name",)}


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "position"]

