from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inbox/", views.inbox, name="inbox"),
    path("project/<str:pk>/", views.project, name="project"),
    path("tag/<str:pk>/", views.tag, name="tag"),
    path("add-task/",views.addTask, name="add-task"),
    path("update-task/<int:pk>/", views.updateTask, name="update-task"),
    path("delete-task/<int:pk>/", views.deleteTask, name="delete-task"),
]
