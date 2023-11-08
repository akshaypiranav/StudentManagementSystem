from django.shortcuts import render,redirect
from .models import StudentDetails
# Create your views here.
def index(request):
    data=StudentDetails.objects.all()
    return render(request,"index.html",{"data":data})

def update(request,id):
    if request.method=="POST":
        data=StudentDetails.objects.get(id=id)
        data.studentName=request.POST.get("name")
        data.studentMail=request.POST.get("mail")
        data.studentRollNumber=request.POST.get("rollNumber")
        data.studentContact=request.POST.get("studentContact")
        data.parentContact=request.POST.get("parentContact")
        if(request.POST.get("profileImage") != "null"):
            data.profileImage=request.POST.get("profileImage")
        data.save()
        return redirect('/')
    if(StudentDetails.objects.filter(id=id)):
        data=StudentDetails.objects.get(id=id)
        return render(request,"update.html",{"data":data})
    else:
        return redirect("/")




def delete(request,id):
    if(StudentDetails.objects.filter(id=id).exists()):
        data=StudentDetails.objects.get(id=id)
        data.delete()
    return redirect("/")

def insert(request):
    if request.method=="POST":
        data=StudentDetails()
        data.studentName=request.POST.get("name")
        data.studentMail=request.POST.get("mail")
        data.studentRollNumber=request.POST.get("rollNumber")
        data.studentContact=request.POST.get("studentContact")
        data.parentContact=request.POST.get("parentContact")
        if(request.POST.get("profileImage") != "null"):
            data.profileImage=request.POST.get("profileImage")
            data.save()
        return redirect('/')
    return render(request,"insert.html")