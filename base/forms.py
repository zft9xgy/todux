from django.forms import ModelForm
from .models import Task, Project, Tag, SimpleTask


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        exclude = ['owner']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class SimpleTaskForm(ModelForm):

    class Meta:
        model = SimpleTask
        fields = "__all__"
        exclude = ['done']
