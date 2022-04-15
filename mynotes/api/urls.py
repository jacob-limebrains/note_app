from django.urls import path
from .views import *

urlpatterns = [
    path("", getRoutes),
    path("notes/", getNotes),
    path("notes/<str:pk>/update", updateNote),
    path("notes/<str:pk>/delete", deleteNote),
    path("notes/<str:pk>", getNote),
]