from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task,Project,Tag
from .forms import TaskForm, ProjectForm, TagForm, TaskFormHtmx
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.http import require_http_methods

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
    user = request.user
    tasks = Task.objects.filter(owner=user, project__isnull=True)

    context = {'tasks': tasks}
    return render(request,'base/inbox.html',context)


@login_required(login_url='login')
def userProfile(request):
    user = request.user
    user_object = get_object_or_404(User, username=user.username)
    
    context = {'user': user}
    return render(request,'base/users/profile.html',context)

# TASK CRUD


@login_required(login_url='login')
def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
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



# # simple task htmx
# def simple(request):
   
#     tasks = SimpleTask.objects.all()

#     context = {'tasks':tasks}
#     return render(request,'base/simple.html',context)

# @require_GET
# def getSimpleTask(request,id):
#     task = get_object_or_404(SimpleTask,id=id)
#     context = {'task':task}
#     return render(request,'base/simple/edit-task.html',context)

# @require_POST
# def createSimpleTask(request):
#     form = SimpleTaskForm(request.POST)
#     if form.is_valid():
#         form.save()
    
#     tasks = SimpleTask.objects.all()

#     context = {'tasks':tasks}
#     return render(request,'base/simple/task_list.html',context)

# @require_http_methods(['DELETE'])
# def deleteSimpleTask(request,id):
    
#     task = get_object_or_404(SimpleTask,id=id)
#     task.delete()
   
#     tasks = SimpleTask.objects.all()

#     context = {'tasks':tasks}
#     return render(request,'base/simple/task_list.html',context)

# @require_POST
# def editSimpleTask(request,id):
#     task = get_object_or_404(SimpleTask,id=id)
#     form = SimpleTaskForm(request.POST,instance=task)
#     if form.is_valid():
#         form.save()
   
#     tasks = SimpleTask.objects.all()

#     context = {'tasks':tasks}
#     return render(request,'base/simple/task_list.html',context)

# @require_POST
# def checkSimpleTask(request,id):

#     task = get_object_or_404(SimpleTask,id=id)
#     task.done = not task.done
#     task.save()
   
#     context = {'task':task}
#     return render(request,'base/simple/simple-task.html',context)

    


# tag crud htmx

def getEditableTagHx(request,id):
    """
    Get current tag and return a edit-tag form.
    """

    tag = get_object_or_404(Tag,id=id)
    context = {'tag':tag}
    return render(request,'components/tags/single-tag-edit.html',context)

@require_http_methods(['POST','GET'])
def createTagHx(request):

    if request.method == 'GET':
        return render(request,'components/tags/single-tag-empty-form.html')

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            
            tag = form.save(commit=False)
            tag.owner = request.user
            tag.save()

            tags = Tag.objects.all()
            context = {'tags':tags} 
            return render(request,'components/tags/list-tags.html',context)


@require_http_methods(['POST'])
def deleteTagHx(request,id):
    tag = Tag.objects.get(id=id)

    if request.user != tag.owner:
        return HttpResponse("You cant do that")

    if request.method == 'POST':
        tag.delete()

        tags = Tag.objects.all()
        context = {'tags':tags} 
        return render(request,'components/tags/list-tags.html',context)

@require_http_methods(['POST','GET'])
def updateTagHx(request,id):

    tag = get_object_or_404(Tag,id=id)

    if request.user != tag.owner:
        return HttpResponse("You cant do that")

    
    if request.method == 'GET':
        context = {'tag':tag}
        return render(request,'components/tags/single-tag-edit.html',context)

    if request.method == 'POST':
        print('dentrod e tag form')
        form = TagForm(request.POST,instance=tag)
        if form.is_valid():
            form.save()

            tags = Tag.objects.all()
            context = {'tags':tags} 
            return render(request,'components/tags/list-tags.html',context)


# project crud htmx

def getEditableProjectHx(request,id):
    """
    Get current project and return a edit-project form.
    """

    project = get_object_or_404(Project,id=id)
    context = {'project':project}
    return render(request,'components/projects/single-project-edit.html',context)

@require_http_methods(['POST','GET'])
def createProjectHx(request):

    if request.method == 'GET':
        return render(request,'components/projects/single-project-empty-form.html')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            projects = Project.objects.all()
            context = {'projects':projects} 
            return render(request,'components/projects/list-projects.html',context)


@require_http_methods(['DELETE'])
def deleteProjectHx(request,id):
    project = Project.objects.get(id=id)

    if request.user != project.owner:
        return HttpResponse("You cant do that")

    if request.method == 'DELETE':
        project.delete()

        projects = Project.objects.all()
        context = {'projects':projects} 
        return render(request,'components/projects/list-projects.html',context)

@require_http_methods(['POST','GET'])
def updateProjectHx(request,id):

    project = get_object_or_404(Project,id=id)

    if request.user != project.owner:
        return HttpResponse("You cant do that")

    
    if request.method == 'GET':
        context = {'project':project}
        return render(request,'components/projects/single-project-edit.html',context)

    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()

            projects = Project.objects.all()
            context = {'projects':projects} 
            return render(request,'components/projects/list-projects.html',context)


# task crud htmx

def getEditableTaskHx(request,id):
    task = get_object_or_404(Task,id=id)
    context = {'task':task}
    
    return render(request,'components/tasks/single-task-empty-form.html',context)

@require_http_methods(['POST','GET'])
def createTaskHx(request):

    if request.method == 'GET':
        return render(request,'components/tasks/single-task-empty-form.html')

    if request.method == 'POST':
        form = TaskFormHtmx(request.POST)
        if form.is_valid():
            
            task = form.save(commit=False)
            task.owner = request.user
            task.save()

            tasks = Task.objects.all()
            context = {'tasks':tasks} 
            return render(request,'components/tasks/list-tasks.html',context)

@require_http_methods(['DELETE'])
def deleteTaskHx(request,id):
    task = Task.objects.get(id=id)

    if request.user != task.owner:
        return HttpResponse("You cant do that")

    if request.method == 'DELETE':
        task.delete()

        tasks = Task.objects.all()
        context = {'tasks':tasks} 
        return render(request,'components/tasks/list-tasks.html',context)

@require_http_methods(['POST','GET'])
def updateTaskHx(request,id):
    task = get_object_or_404(Task,id=id)

    if request.user != task.owner:
        return HttpResponse("You cant do that")

    
    if request.method == 'GET':
        context = {'task':task}
        return render(request,'components/tasks/single-task-edit.html',context)

    if request.method == 'POST':
        form = TaskFormHtmx(request.POST,instance=task)
        if form.is_valid():
            form.save()

            tasks = Task.objects.all()
            context = {'tasks':tasks} 
            return render(request,'components/tasks/list-tasks.html',context)


@require_POST
def checkTask(request,id):

    task = get_object_or_404(Task,id=id)
    task.done = not task.done
    task.save()
   
    tasks = Task.objects.all()
    context = {'tasks':tasks} 
    return render(request,'components/tasks/list-tasks.html',context)