from django.contrib import admin
from .models import Task,Project,Tag, SimpleTask


admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(SimpleTask)