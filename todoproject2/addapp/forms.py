from todoapp1.models import Task
from django import forms
class todoform(forms.ModelForm):
     class Meta:
       model=Task
       fields=['taskname','priority','date']

