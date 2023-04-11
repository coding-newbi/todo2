from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from addapp.forms import todoform
from todoapp1.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=Task
    template_name='home1.html'
    context_object_name ='task1'

class taskdetailview(DetailView):
    model = Task
    template_name = 'detailview.html'
    context_object_name = 't'
class taskupdateview(UpdateView):
    model = Task
    template_name = 'updateview.html'
    context_object_name = 't'
    fields = ['taskname','priority','date']
    def get_success_url(self):
        return reverse_lazy('classdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 't'
    success_url = reverse_lazy('classview')


# Create your views here.
def add1(request):
    task1=Task.objects.all()
    if request.method=='POST':
        taskname=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(taskname=taskname,priority=priority,date=date)
        task.save()
    return render(request,'home1.html',{'task1':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/add1')
    return render(request,'delete.html')
def update(request,taskid):
    task=Task.objects.get(id=taskid)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/add1')
    return render(request,'edit.html',{'f':f,'task':task})
