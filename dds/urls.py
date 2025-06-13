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
    path("edit_status/<int:id>", views.edit_status),
    path("add_status", views.add_status),
    path("delete_status/<int:id>", views.delete_status),
    path("edit_operation_type/<int:id>", views.edit_operation_type),
    path("add_operation_type", views.add_operation_type),
    path("delete_operation_type/<int:id>", views.delete_operation_type),
    path("edit_category/<int:id>", views.edit_category),
    path("add_category", views.add_category),
    path("delete_category/<int:id>", views.delete_category),
    path("edit_subcategory/<int:id>", views.edit_subcategory),
    path("add_subcategory", views.add_subcategory),
    path("delete_subcategory/<int:id>", views.delete_subcategory),
    path('admin/', admin.site.urls),
]
