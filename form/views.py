from django.shortcuts import render
from form.models import Info

# Create your views here.

def index(request):

    try:

        if request.method=="POST":
            Student_Name=request.POST.get("Student_Name")
            Father_Name=request.POST.get("Father_Name")
            Mother_Name=request.POST.get("Mother_Name")
            Date_Of_Birth=request.POST.get("Date_Of_Birth")
            gender=request.POST.get("gender")
            roll=request.POST.get("roll")
            branch=request.POST.get("branch")
            year=request.POST.get("year")
            Contact_Number=request.POST.get("Contact_Number")
            Father_Contact_Number=request.POST.get("Father_Contact_Number")
            Mother_Contact_Number=request.POST.get("Mother_Contact_Number")
            Aadhar_Number=request.POST.get("Aadhar_Number")
            Address=request.POST.get("Address")

            info=Info(Student_Name=Student_Name, gender=gender, Father_Name=Father_Name, 
            Mother_Name=Mother_Name, Date_Of_Birth=Date_Of_Birth, roll=roll, branch=branch, year=year, 
            Contact_Number=Contact_Number, Father_Contact_Number=Father_Contact_Number, Mother_Contact_Number=Mother_Contact_Number,
            Aadhar_Number=Aadhar_Number,Address=Address)

            info.save()
            
    except:
        return render(request, "error.html")

    return render(request, "index.html")