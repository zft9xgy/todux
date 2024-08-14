from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("login/",views.loginPage,name="login"),
    #path("profile/",views.userProfile,name="profile"),
    #path("register/",views.registerPage,name="register"),
    #path("logout/",views.logoutPage,name="logout"),
    #path("inbox/", views.inbox, name="inbox"),
    
    path("tag/<int:pk>/", views.tag, name="tag"),
    path("add-task/",views.addTask, name="add-task"),
    path("update-task/<int:pk>/", views.updateTask, name="update-task"),
    path("delete-task/<int:pk>/", views.deleteTask, name="delete-task"),
    
    path("project/<int:pk>/", views.project, name="project"),
    path("create-project/", views.createProject, name="create-project"),
    path("update-project/<int:pk>/", views.updateProject, name="update-project"),
    path("delete-project/<int:pk>/", views.deleteProject, name="delete-project"),

    path("create-tag/", views.createTag, name="create-tag"),
    path("update-tag/<int:pk>/", views.updateTag, name="update-tag"),
    path("delete-tag/<int:pk>/", views.deleteTag, name="delete-tag"),
    


    # tag htmx
    path("tag/get/", views.getEditableTagHx, name="tag-get"),
    path("tag/create/", views.createTagHx, name="tag-create"),
    path("tag/delete/<str:id>", views.deleteTagHx, name="tag-delete"),
    path("tag/update/<str:id>", views.updateTagHx, name="tag-update"),

    # project htmx
    path("project/get/", views.getEditableProjectHx, name="project-get"),
    path("project/create/", views.createProjectHx, name="project-create"),
    path("project/delete/<str:id>", views.deleteProjectHx, name="project-delete"),
    path("project/update/<str:id>", views.updateProjectHx, name="project-update"),

    # task htmx
    path("task/get/<str:id>", views.getEditableTaskHx, name="task-get"),
    path("task/create/", views.createTaskHx, name="task-create"),
    path("task/delete/<str:id>", views.deleteTaskHx, name="task-delete"),
    path("task/update/<str:id>", views.updateTaskHx, name="task-update"),
    path("task/check/<str:id>", views.checkTask, name="task-check"),


    


]
