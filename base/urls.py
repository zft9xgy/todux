from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.loginPage,name="login"),
    path("profile/",views.userProfile,name="profile"),
    path("register/",views.registerPage,name="register"),
    path("logout/",views.logoutPage,name="logout"),
    path("inbox/", views.inbox, name="inbox"),
    path("project/<int:pk>/", views.project, name="project"),
    path("tag/<int:pk>/", views.tag, name="tag"),
    path("add-task/",views.addTask, name="add-task"),
    path("update-task/<int:pk>/", views.updateTask, name="update-task"),
    path("delete-task/<int:pk>/", views.deleteTask, name="delete-task"),

    path("update-project/<int:pk>/", views.updateProject, name="update-project"),
    path("create-project/", views.createProject, name="create-project"),
    path("delete-project/<int:pk>/", views.deleteProject, name="delete-project"),

    path("create-tag/", views.createTag, name="create-tag"),
    path("delete-tag/<int:pk>/", views.deleteTag, name="delete-tag"),
    path("update-tag/<int:pk>/", views.updateTag, name="update-tag"),

    path("simple/", views.simple, name="simple"),
    path("simple/create", views.createSimpleTask, name="simple-create"),
    path("simple/delete/<str:id>", views.deleteSimpleTask, name="simple-delete"),
    path("simple/get/<str:id>", views.getSimpleTask, name="simple-get"),
    path("simple/edit/<str:id>", views.editSimpleTask, name="simple-edit"),
    path("simple/check/<str:id>", views.checkSimpleTask, name="simple-check"),

    


]
