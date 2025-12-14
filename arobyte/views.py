from django.shortcuts import render, redirect, get_object_or_404
from .models import Volunteer, Contact, Cause, Donate, Blog, Announcement
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
import openpyxl
from openpyxl.styles import Font, PatternFill
from datetime import datetime

# Create your views here.
def index(request):
    causes=Cause.objects.all()
    return render(request,'index.html',{"causes":causes})

def submit_valunteer(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST.get('message')
        college_name=request.POST['college_name']
        preprofessional=request.POST['preprofessional']

        volunteer=Volunteer.objects.create(name=name,email=email,subject=subject,message=message,college_name=college_name,preprofessional=preprofessional)
        volunteer.save()
        messages.success(request, "Your volunteer application has been submitted successfully!")
        return redirect('/')
    else:
        return redirect('/')

def contact(request):
    if request.method == "POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        message=request.POST.get('message')

        contact=Contact.objects.create(name=f"{f_name}  {l_name}",email=email,message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/contact/')
    return render(request, 'contact.html')

def volunteer(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST.get('message')
        college_name=request.POST['college_name']
        preprofessional=request.POST['preprofessional']

        volunteer=Volunteer.objects.create(name=name,email=email,subject=subject,message=message,college_name=college_name,preprofessional=preprofessional)
        volunteer.save()
        messages.success(request, "Your volunteer application has been submitted successfully!")
        return redirect('/volunteer/')
    return render(request, 'volunteer.html')

def donate(request,id):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        amount=request.POST.get('amount')

        cause=Cause.objects.get(id=id)
        cause.raised=cause.raised+float(amount)
        cause.goal=cause.goal-float(amount)
        cause.save()
        donation=Donate.objects.create(name=name,email=email,amount=float(amount))
        donation.save()
        return redirect('/')
    else:
        cause=Cause.objects.get(id=id)
        return render(request,'donate.html',{"cause":cause})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def about(request):
    return render(request, 'about.html')

def causes(request):
    causes = Cause.objects.all()
    return render(request, 'causes.html', {'causes': causes})

def announcement_list(request):
    today = timezone.now().date()
    announcements = Announcement.objects.filter(
        is_active=True
    ).filter(
        Q(end_date__isnull=True) | Q(end_date__gte=today)
    ).order_by('-priority', '-created_at')
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, 'announcements/announcement_detail.html', {'announcement': announcement})