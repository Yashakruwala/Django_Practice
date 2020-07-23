from django.db import models

# Create your models here.

class jobsearch(models.Model):
 job = models.CharField(max_length=100)
 company_name = models.CharField(max_length=100)

def _str_(self):
    return self.job

class Company_requirements(models.Model):
 jobsearch = models.ForeignKey(jobsearch, on_delete = models.CASCADE)
 perks= models.CharField(max_length=200)
 Skill_requirement= models.CharField(max_length=200)
 #filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

 
def _str_(self):
    return self.job
