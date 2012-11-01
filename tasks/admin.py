from django.contrib import admin
from tasks.models import Task, Project
from django.contrib.admin.options import ModelAdmin

class ProjectAdmin(ModelAdmin):
    readonly_fields = ("created", "modified",)

class TaskAdmin(ModelAdmin):
    readonly_fields = ("created", "modified", 'percent_update_time',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)
