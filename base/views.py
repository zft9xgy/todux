from django.shortcuts import render,redirect, get_object_or_404
from .models import Task,Project,Tag
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all()
    tags = Tag.objects.all()
    projects = Project.objects.all()
    context = {'tasks':tasks,'projects':projects,'tags':tags}
    return render(request,'base/home.html',context)

def project(request,pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request,'base/project.html',context)

def tag(request,pk):
    
    tag = get_object_or_404(Tag, pk=pk)

    # Obtén todas las tareas asociadas a la etiqueta
    tasks = Task.objects.filter(tags=tag)

    context = {'tasks':tasks}
    return render(request,'base/tag.html',context)

def inbox(request):
    return render(request,'base/inbox.html')


def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/add_task.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/add_task.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    # form = TaskForm(instance=task)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'obj':task}
    return render(request,'base/delete.html',context)