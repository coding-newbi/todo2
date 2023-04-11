from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy


from .models import Task


# Create your views here.
#def show(request):
 #   return HttpResponse('hello')
def add(request):
   if request.method=='POST':
       taskname=request.POST.get('taskname','')
       priority=request.POST.get('priority','')
       date=request.POST.get('date')


       task=Task(taskname=taskname,priority=priority,date=date)
       task.save()
   return render(request,'home.html')
def details(request):
   task=Task.objects.all()
   return render(request,'details.html',{'task':task})
