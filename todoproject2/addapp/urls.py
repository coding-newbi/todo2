from django.urls import path

from addapp import views


urlpatterns = [
     path('',views.add1,name='add1'),
     path('delete/<int:taskid>/',views.delete,name='delete'),
     path('update/<int:taskid>/',views.update,name='update'),
     path('classview/',views.tasklistview.as_view(),name='classview'),
     path('classdetail/<int:pk>/',views.taskdetailview.as_view(),name='classdetail'),
     path('classupdate/<int:pk>/',views.taskupdateview.as_view(),name='classupdate'),
     path('classdelete/<int:pk>/',views.taskdeleteview.as_view(),name='classdelete'),

]