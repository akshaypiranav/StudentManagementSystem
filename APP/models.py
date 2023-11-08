from django.db import models
import datetime
import os
# Create your models here.
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class StudentDetails(models.Model):
    studentName=models.CharField(max_length=30,blank=False,null=False)
    studentRollNumber=models.CharField(max_length=30,blank=False,null=False)
    studentMail=models.CharField(max_length=30,blank=False,null=False)
    studentContact=models.CharField(max_length=30,blank=False,null=False)
    parentContact=models.CharField(max_length=30,blank=False,null=False)
    profileImage=models.ImageField(upload_to=getFileName,null=True,blank=True)
    class Meta:
        db_table='studentDetails'
