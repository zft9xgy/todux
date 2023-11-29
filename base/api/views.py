from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Task
from .serializers import TaskSerializer
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/tasks',
        'GET /api/tasks/:id',
    ]
    return Response(routes)

@login_required(login_url='login')
@api_view(['GET'])
def getTasks(request):
    user = request.user
    tasks = Task.objects.filter(owner=user)
    #tasks = user.task_set.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['GET'])
def getTask(request,pk):
    user = request.user
    task = Task.objects.get(owner=user,pk=pk)
    #task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)