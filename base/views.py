from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task,Project,Tag
from .forms import TaskForm, ProjectForm, TagForm

@login_required(login_url='login')
def home(request):
    user = request.user

    tasks = user.task_set.all()
    tags = user.tag_set.all()
    projects = user.project_set.all()

    context = {'tasks':tasks,'projects':projects,'tags':tags}
    return render(request,'base/home.html',context)

def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User doesnt exist!")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"User or password is wrong!")

    context = {'page': page}
    return render(request,'base/users/login_register.html',context)

def registerPage(request):
    page = "register"
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Error en la creación del usuario.")

    context = {'page':page,'form':form}
    return render(request,'base/users/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def project(request,pk):
    user = request.user
    #project = Project.objects.get(id=pk)
    project = user.project_set.filter(id=pk).first()

    if project is None:
        return HttpResponse("Project not found or you don't have access to it!")

    # tasks = Task.objects.filter(project=pk)
    tasks = project.task_set.all()
    
    context = {'project':project,'tasks':tasks}
    return render(request,'base/project.html',context)

@login_required(login_url='login')
def tag(request,pk):
    
    user = request.user
    tag = user.tag_set.filter(pk=pk).first()
    # tag = get_object_or_404(Tag, pk=pk)
    if project is None:
        return HttpResponse("Tag not found or you don't have access to it!")

    # Obtén todas las tareas asociadas a la etiqueta
    tasks = Task.objects.filter(tags=tag)

    context = {'tasks': tasks}
    return render(request,'base/tag.html',context)

@login_required(login_url='login')
def inbox(request):
    return render(request,'base/inbox.html')



# TASK CRUD


@login_required(login_url='login')
def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/add_task.html',context)

@login_required(login_url='login')
def updateTask(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.user != task.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/add_task.html',context)

@login_required(login_url='login')
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)

    if request.user != task.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'obj':task}
    return render(request,'base/delete.html',context)




# Project CRUD

@login_required(login_url='login')
def createProject(request):
    user = request.user
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = user
            project.save()
            return redirect('project',pk=project.pk) 

    context = {'form':form} 
    return render(request,'base/create_project.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)

    if request.user != project.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        project.delete()
        return redirect('home')

    context = {'obj':project}
    return render(request,'base/delete.html',context)

@login_required(login_url='login')
def updateProject(request,pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.user != project.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/add_task.html',context)


# tag CRUD

@login_required(login_url='login')
def createTag(request):
    user = request.user
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            tag = form.save(commit=False)
            tag.owner = user
            tag.save()
            #return redirect('tag',pk=tag.pk) 
            return redirect('home')

    context = {'form':form} 
    return render(request,'base/tags/create_tag.html',context)


@login_required(login_url='login')
def deleteTag(request,pk):
    tag = Tag.objects.get(id=pk)

    if request.user != tag.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        tag.delete()
        return redirect('home')

    context = {'obj':tag}
    return render(request,'base/delete.html',context)

@login_required(login_url='login')
def updateTag(request,pk):

    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)

    if request.user != tag.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form.as_p}
    return render(request,'base/tags/create_tag.html',context)