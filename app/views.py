from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

def portfolio(request):
    profile = Profile.objects.first()
    link = Links.objects.first()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("_replyto")
        message = request.POST.get("message")

        subject = f"New Contact Message from {name}"
        body = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
        messages.success(request, "✅ Your message has been sent successfully!")
        return redirect("portfolio")
    return render(request, 'index.html', {
        'profile': profile,
        'link':link,
        'experiences': Experience.objects.filter(profile=profile),
        'projects': Project.objects.filter(profile=profile),
        'certificates': Certificate.objects.filter(profile=profile),
        'skills_technical': TechnicalSkill.objects.filter(profile=profile),
        'skills_soft': SoftSkill.objects.filter(profile=profile),
    })


@login_required(login_url='login')
def dashboard(request):
    profile = Profile.objects.first()
    return render(request, 'dashboard.html', {
        'profile': profile,
        'experiences': Experience.objects.filter(profile=profile),
        'projects': Project.objects.filter(profile=profile),
        'skills_technical': TechnicalSkill.objects.filter(profile=profile),
        'skills_soft': SoftSkill.objects.filter(profile=profile),
        'certificates': Certificate.objects.filter(profile=profile),
    })


def add_item(request, model_name):
    profile = Profile.objects.first()
    if not profile:
        return HttpResponse("❗ Please create a Profile first before adding other items.")

    form_map = {
        'experience': ExperienceForm,
        'project': ProjectForm,
        'certificate': CertificateForm,
        'technicalskill': TechnicalSkillForm,
        'softskill': SoftSkillForm,
    }

    if model_name not in form_map:
        return HttpResponse("Invalid item type.")

    form = form_map[model_name](request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.profile = profile  # ✅ this line sets the foreign key
        obj.save()
        return redirect('dashboard')

    return render(request, 'item_form.html', {'form': form, 'type': model_name})




def delete_item(request, model_name, id):
    model_map = {
        'experience': Experience,
        'project': Project,
        'certificate': Certificate,
        'technicalskill': TechnicalSkill,
        'softskill': SoftSkill,
    }
    obj = get_object_or_404(model_map[model_name], id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('dashboard')

    return render(request, 'confirm_delete.html', {'item': obj})


# === LOGIN ===
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


# === LOGOUT ===
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
