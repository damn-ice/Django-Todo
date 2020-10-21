from django.urls import path
from . import views


app_name = "to_do_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("del/<int:todo_id>/", views.delete, name="del")
]
