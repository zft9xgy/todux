from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inbox/", views.inbox, name="inbox"),
    path("project/<str:pk>/", views.project, name="project"),
]
