
from django.urls import path

from todoapp1 import views

urlpatterns = [


 path('',views.add,name='see'),
  path('details/',views.details,name='details'),

]