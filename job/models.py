from django.db import models

# Create your models here.
JOB_TYPE=(
    ('FULL TIME','FULLE TIME'),
    ('PART TIME','PART TIME'),
)

def image_upload(instance,filename):
    imagename,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):
    title= models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=100)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=1)
    experience=models.IntegerField(default=0)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    #image=models.ImageField( upload_to='jobs/')
    image=models.ImageField( upload_to='image_upload')
    
    def __str__(self):
     return self.title
class category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self) :
       return self.name 