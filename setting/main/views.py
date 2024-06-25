from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def one(request):
    tasks = Task.objects.order_by('-id')[:]
    return render(request, 'main/one.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def two(request):
    return render(request, 'main/two.html')


def tree(request):
    return render(request, 'main/tree.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была не верна'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
