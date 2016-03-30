from django.shortcuts import render, redirect
from brandid.models import *
from brandid.forms import *

def home(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = request.POST.get('name')
            request.session['full_name'] = full_name
            contact_form.save()
            return redirect('brandid:success')
        else:
            print contact_form.errors
    else:
        contact_form = ContactForm()
    context = {'contact_us':contact_form}
    return render(request, 'brand/home.html', context)
    
def success(request):
    context = {'full_name':request.session['full_name']}
    full_name = None
    return render(request, 'brand/successful.html', context)

def startup_mvps(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = request.POST.get('name')
            request.session['full_name'] = full_name
            contact_form.save()
            return redirect('brandid:success')
        else:
            print contact_form.errors
    else:
        contact_form = ContactForm()
    context = {'contact_us':contact_form }
    return render(request, 'brand/startups_mvps.html', context)

def services(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = request.POST.get('name')
            request.session['full_name'] = full_name
            contact_form.save()
            return redirect('brandid:success')
        else:
            print contact_form.errors
    else:
        contact_form = ContactForm()
    return render(request, 'brand/services.html', {'contact_us':contact_form})


def about_us(request):
    return render(request, 'brand/about_us.html', {}) 


def logo_design(request):
    service = "logo_design"
    return render(request, 'brand/all_services.html', {'logo_design':service})

def web_design(request):
    service = "web_design"
    return render(request, 'brand/all_services.html', {'web_design':service})

def mobile_app_design(request):
    service = "mobile_app_design"
    return render(request, 'brand/all_services.html', {'mobile_app_design':service})

def print_design(request):
    service = "print_design"
    return render(request, 'brand/all_services.html', {'print_design':service})

def corperate_branding(request):
    service = "corperate_branding"
    return render(request, 'brand/all_services.html', {'corperate_branding':service})

def social_media_branding(request):
    service = "social_media_branding"
    return render(request, 'brand/all_services.html', {'social_media_branding':service})

def web_development(request):
    service = "web_development"
    return render(request, 'brand/all_services.html', {'web_development':service})

def mobile_app_development(request):
    service = "mobile_app_development"
    return render(request, 'brand/all_services.html', {'mobile_app_development':service})

def ecommerce_development(request):
    service = "ecommerce_development"
    return render(request, 'brand/all_services.html', {'ecommerce_development':service})

def enterprise_software(request):
    service = "enterprise_software"
    return render(request, 'brand/all_services.html', {'enterprise_software':service})

def cloud_deployment(request):
    service = "cloud_deployment"
    return render(request, 'brand/all_services.html', {'cloud_deployment':service})

def database_migration(request):
    service = "database_migration"
    return render(request, 'brand/all_services.html', {'database_migration':service})

def ecommerce(request):
    service = "ecommerce"
    return render(request, 'brand/all_services.html', {'ecommerce':service})

def churches(request):
    service = "churches"
    return render(request, 'brand/all_services.html', {'churches':service})

def corperate(request):
    service = "corperate"
    return render(request, 'brand/all_services.html', {'corperate':service})

def small_businessess(request):
    service = "small_businessess"
    return render(request, 'brand/all_services.html', {'small_businessess':service})

def education(request):
    service = "education"
    return render(request, 'brand/all_services.html', {'education':service})

def government(request):
    service = "government"
    return render(request, 'brand/all_services.html', {'government':service})

def ngos(request):
    service = "ngos"
    return render(request, 'brand/all_services.html', {'ngos':service})

def startups(request):
    service = "startups"
    return render(request, 'brand/all_services.html', {'startups':service})

