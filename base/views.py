from django.shortcuts import render
from .models import Task,Project

# Create your views here.
# Controlador manejo de la logica del programa



def home(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    context = {'tasks':tasks,'projects':projects}
    return render(request,'base/home.html',context)


def project(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request,'base/project.html',context)


def inbox(request):
    return render(request,'base/inbox.html')
