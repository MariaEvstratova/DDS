from django.contrib import admin
from django.urls import path
from . import views


# Добавление url путей
urlpatterns = [
    path("", views.index),
    path("dicts", views.dicts),
    path("edit_operation/<int:id>", views.edit_operation),
    path("add_operation", views.add_operation),
    path("delete_operation/<int:id>", views.delete_operation),
    path('admin/', admin.site.urls),
]
