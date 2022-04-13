from asyncio import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.form import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request, ("New Task Added!")) 
        return redirect('todolist')
    else:
        alltasks = Tasklist.objects.filter(owner = request.user)
        pagi = Paginator(alltasks, 5)
        page = request.GET.get('pg')
        alltasks = pagi.get_page(page)

        return render(request, 'todolist.html', {'alltasks': alltasks})

def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
        return redirect('todolist')
    else:
        messages.error(request, ("You are not allowed damn man!")) 
   

def complete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
        return redirect('todolist')
    else:
        messages.error(request, ("You are not allowed damn man!"))

def uncomplete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
        return redirect('todolist')
    else:
        messages.error(request, ("You are not allowed damn man!"))

def edit_task(request, task_id):
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task edited")) 
        return redirect('todolist')
    else:
        taskobj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'taskobj': taskobj})

def index(request):
    context = {
        'index_text':"ya alf welcome ya index!",
        }
    return render(request, 'index.html', context)

@login_required
def contact(request):
    context = {
        'contact_text':"Welcome to contact page!",
        }
    return render(request, 'contact.html', context)

@login_required
def about(request):
    context = {
        'about_text':"Welcome to about page!",
        }
    return render(request, 'about.html', context)
