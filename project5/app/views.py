from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO = Todo(title=title,desc=desc)
        TO.save()
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    return render(request,'home.html',d)

sno=0
def update(request):
    if  request.method =="GET":
        global sno
        sno = request.GET.get('pk')
        TO = Todo.objects.get(sno=sno)
        d = {'TO':TO}
        return render(request,'update.html')
    elif request.method =="POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO = Todo.objects.filter(sno=sno)
        TO.update(title=title,desc=desc)
        alltodos = Todo.objects.all()
        d ={'alltodos':alltodos}
        return render(request,'home.html',d)
    
def delete(request):
    sno = request.GET.get('pk')
    TO = Todo.objects.filter(sno=sno)
    TO.delete()
    alltodos = Todo.objects.all()
    d= {'alltodos':alltodos}
    return render(request,'home.html',d)