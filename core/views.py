from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, ContactMessage

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.order_by('-created_at')[:3]
    return render(request, 'core/home.html', {'skills': skills, 'projects': projects})

def portfolio(request):
    # Retrieve all projects
    projects = Project.objects.order_by('-created_at')
    return render(request, 'core/portfolio.html', {'projects': projects})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'core/about.html', {'skills': skills})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
    return render(request, 'core/contact.html')
