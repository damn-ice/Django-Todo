from django.shortcuts import render, redirect
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    context = {"todos": todos}
    return render(request, "to_do_app/index.html", context)

def add(request):
    content = request.POST["todo"]
    to_do = ToDo.objects.create(text=content)
    return redirect("to_do_app:index")

def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect("to_do_app:index")



# Create your views here.
