from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name ='index'),
    path('jobsearch/',views.jobsearch, name='jobsearch'),
    path('info/<str:pk>/',views.details,name='details')

    

]