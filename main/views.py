from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project, Skill
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Сообщение от {name}',
                message,
                email,
                ['goka4ka2008@gmail.com'],  
            )
            success = True
            form = ContactForm()

    return render(request, 'main/home.html', {
        'projects': projects,
        'skills': skills,
        'form': form,
        'success': success,
    })