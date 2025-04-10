from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'pages/home.html')

def projects(request):
    return render(request, 'pages/projects.html')

def experience(request):
    return render(request, 'pages/experience.html')

def experience_detail(request, slug):
    return render(request, f'experience_details/{slug}.html')

def education(request):
    return render(request, 'pages/education.html')

def education_detail(request, slug):
    return render(request, f'education_details/{slug}.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid data")
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            message_body = f"this is an email from your portofolio\nName:{name}\nEmail:{email}\nMessage:\n{message}"

            send_mail(
                "Email from Portfolio",
                message_body,
                email,
                ['hershand55@gmail.com']
            )
        else:
            print("Invalid form Data")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {"form": form})