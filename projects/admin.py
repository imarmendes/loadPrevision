from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName', 'responsible', 'address', 'art', 'autor')
    search_fields = ('projectName',)
    ordering = ['projectName']

