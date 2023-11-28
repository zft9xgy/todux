from django.forms import ModelForm
from .models import Task, Project, Tag


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']