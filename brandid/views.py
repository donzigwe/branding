from django.shortcuts import render, redirect, get_object_or_404
from brandid.models import *
from brandid.forms import *
import datetime
from datetime import timedelta, date
import random

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

def logo_id():
    date = str(datetime.datetime.now())[2:10]
    date = date.replace('-', '')
    randnum = str(random.random())[4:8]
    id_num = 'logo' + date + randnum
    return id_num

print logo_id()

def logo_company(request):
    if request.method == "POST":
        company_form = LogoCompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            my_logo = logo_id()
            company.logo_id = my_logo
            request.session['my_logo'] = my_logo
            company.save()
            print 'I want to print this ID', request.session['my_logo']
            return redirect('brandid:logo_project')
        else:
            print company_form.errors
    else:
        company_form = LogoCompanyForm()
    logo_design = 'logo_design1'
    context = {'company_form':company_form, 'logo_design1':logo_design}
    return render(request, 'brand/logo_form.html', context)

def logo_project(request):
    mycompany = get_object_or_404(LogoCompany, logo_id=request.session['my_logo'])
    if request.method == "POST":
        project_form = LogoProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.company = mycompany
            project.save()
            return redirect('brandid:logo_design')
        else:
            print 'print my errors', project_form.errors
    else:
        project_form = LogoProjectForm()
    logo_design = 'logo_design1'
    context = {'project_form':project_form, 'logo_design1':logo_design}
    return render(request, 'brand/logo_form.html', context)


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

