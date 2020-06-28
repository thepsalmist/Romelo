from django.urls import path
from .views import home, project_detail

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("project/<slug:slug>/", project_detail, name="project"),
]
