from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator

# Create your views here.
# -=--------=---=----------=--=------PAGES--=---=------=---
# HOME
def home(request):
    return render(request,"home/index.html")

# CONTACT US
def contact(request):
    # from home.forms import ContactUsForm
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'We have saved your Contact Us request and will contact to you as soon as possible.')
    return render(request,"home/contact.html")

# ABOUT
def about(request):
    return render(request,"home/about.html")

def termsconditions(request):
    return render(request,"home/terms.html")

def disclaimer(request):
    return render(request,"home/disclaimer.html")

# POLICY
def privacypolicy(request):
    return render(request,"home/privacypolicy.html")

def refundpolicy(request):
    return render(request,"home/refundpolicy.html")


# DASHBOARD PAGES

def pricing(request):
    context = {
    }
    return render(request,"home/pricing.html",context)

def dashboard(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,"dashboard/dashboard.html",context)


def course(request):
    courses = Course.objects.all()
    context = {
        'courses':courses,
    }
    return render(request,"dashboard/courseselect.html",context)


def courses(request,id):
    course = Course.objects.all()
    current_course = Course.objects.get(id=id)
    chapters = Chapter.objects.filter(course=current_course)
    context = {
        "chapters":chapters,
        "course":course,
        "current_course":current_course,
    }
    return render(request,"dashboard/courses.html",context)


def chapters(request,cou):
    current_course = Course.objects.get(id=cou)
    chapters = Chapter.objects.filter(course=current_course)
    paginator = Paginator(chapters,1)
    chapter_number=request.GET.get('page')
    current_chapter = paginator.get_page(chapter_number)
    context = {
        "cou":cou,
        "chapters":chapters,
        "current_course":current_course,
        "current_chapter":current_chapter,
    }
    return render(request,"dashboard/chapters.html",context)

