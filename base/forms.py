from django.forms import ModelForm
from .models import Task, Project, Tag


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        exclude = ['owner']

class TaskFormHtmx(ModelForm):

    class Meta:
        model = Task
        fields = ['title']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


