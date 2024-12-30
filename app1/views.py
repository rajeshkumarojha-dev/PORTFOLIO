from django.shortcuts import render
from app1.forms import ContactForm
from app1.models import Portfolio
# Create your views here.

def home(request):
    return render(request, 'app1/index.html')

def resume(request):
    return render(request, 'app1/index-resume.html')

def project(request):
    return render(request, 'app1/index-project.html')
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            description=request.POST['description']
            user=Portfolio(first_name=fname,last_name=lname,email=email,description=description)
            user.save()
    else:
        form=ContactForm()
    return render(request, 'app1/index-contact.html')
