from django.shortcuts import render
from .models import Job  
# Create your views here.
def job_list(request) :
    job_list=Job.objects.all()
    context={'jobs':job_list}
    return render(request,'job/job_list.html',context) 
    
    
def job_detaills(request,id):
   job_detaills=Job.objects.get(id=id)
   context={'joob':job_detaills}
   return render(request,'job/job_detaills.html',context)