from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
import os
from django.conf import settings

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save to file
            with open('submissions.txt', 'a') as f:
                f.write(f'Name: {name}\n')
                f.write(f'Email: {email}\n')
                f.write(f'Message: {message}\n')
                f.write('--- New Incoming Message ---\n')

            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def skills(request):
    return render(request, 'portfolio/skills.html')

def experience(request):
    return render(request, 'portfolio/experience.html')