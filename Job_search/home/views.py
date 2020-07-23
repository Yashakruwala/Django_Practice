from django.shortcuts import render
from . models import jobsearch,Company_requirements
# Create your views here.
def index(request):
    jobs = jobsearch.objects.all()
    return render(request, 'index.html',{'jobs': jobs})

def jobsearch(request):
   Job = request.POST['search']
   
   jobs= jobsearch.objects.get(job= Job)
   return render(request,'index.html',{'jobs': jobs})

def details(request,pk):
    requirement= Company_requirements.objects.get(id=pk)

    return render(request,'search.html',{'requirement': requirement})