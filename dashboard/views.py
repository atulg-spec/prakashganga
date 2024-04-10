from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from django.conf import settings
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime,timedelta
import razorpay
User = get_user_model()
# -=--------=---=----------=--=------PAGES--=---=------=---
# HOME
def home(request):
    updates = Updates.objects.all()
    context = {
        'updates':updates,
    }
    return render(request,"home/index.html",context)

# CONTACT US
def contact(request):
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'We have saved your Contact Us request and will reach to you as soon as possible.')
        return render(request,'home/message.html')
    context = {
        'form':form
    }
    return render(request,"home/contact.html",context)

def investment(request):
    form = InvestmentForm(request.POST)
    if form.is_valid():
        formob = form.save(commit=False)
        formob.subject = 'For Investment Enquire'
        formob.save()
        messages.success(request,'We have submitted your request and try will reach to you as soon as possible.')
        return render(request,'home/message.html')
    context = {
        'form':form
    }
    return render(request,"home/investment.html",context)

def careers(request):
    form = InvestmentForm(request.POST)
    if form.is_valid():
        formob = form.save(commit=False)
        formob.subject = 'Job seeking'
        formob.save()
        messages.success(request,'We have submitted your request and try will reach to you as soon as possible.')
        return render(request,'home/message.html')
    context = {
        'form':form
    }
    return render(request,"home/careers.html",context)

def opendemat(request):
    form = OpenDematForm(request.POST)
    if form.is_valid():
        formob = form.save(commit=False)
        formob.subject = 'Open Demat Account'
        formob.message = 'I want to open a Demat Account in Motilal Oswal with you'
        formob.save()
        messages.success(request,'We have saved your Demat Account opening request and will reach to you as soon as possible.')
        return render(request,'home/message.html')
    context = {
        'form':form
    }
    return render(request,"home/opendemat.html",context)


# ABOUT
def about(request):
    return render(request,"home/about.html")

def termsofuse(request):
    return render(request,"home/terms.html")

def disclaimer(request):
    return render(request,"home/disclaimer.html")

# POLICY
def privacypolicy(request):
    return render(request,"home/privacypolicy.html")

def refundpolicy(request):
    return render(request,"home/refundpolicy.html")


# DASHBOARD PAGES
# @login_required
def pricing(request):
#    if request.user.is_suscribed:
#        return redirect('/course')
    # if request.user.is_suscribed:
    #     return redirect('/course')
    # client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))
    # payment = client.order.create({'amount':1990000,'currency':'INR','payment_capture':1})
    # request.user.order_id = payment['id']
    # request.user.save()
    # print(payment)
    context = {
        # 'payment':payment,
        'key':settings.RAZORPAY_KEY,
    }
    return render(request,"home/pricing.html",context)

@csrf_exempt
def payment_status(request):
    if request.method == 'POST':
        try:
            a = request.POST
            data = {}
            order_id = ''
            for key,val in a.items():
                if key == 'razorpay_order_id':
                    data['razorpay_order_id'] = val
                    order_id = val
                elif key == 'razorpay_payment_id':
                    data['razorpay_payment_id'] = val
                elif key == 'razorpay_signature':
                    data['razorpay_signature'] = val
    
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))
            check = client.utility.verify_payment_signature(data)
            print('-=-=-=-=-=-=-=-')
            print(check)
            print('-=-=-=-=-=-=-=-')
            if check:
                user = User.objects.filter(order_id=order_id).first()
                user.is_suscribed = True
                user.suscribed_date = timezone.now()
                user.expiry_date = timezone.now() + timedelta(days=30)
                user.save()
                context = {
                    'check':check
                }
                return render(request,"home/payment.html",context)
        except Exception as e:
            print(f'error {e}')
            return redirect('/pricing')
    




        print(order_id)


def dashboard(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,"dashboard/dashboard.html",context)

@login_required
def course(request):
    courses = Course.objects.all()
    updates = Updates.objects.all()
    context = {
        'updates':updates,
        'courses':courses,
    }
    return render(request,"dashboard/courseselect.html",context)

@login_required
def courses(request,id):
    if not request.user.is_suscribed:
        return redirect('/pricing')
    course = Course.objects.all()
    current_course = Course.objects.get(id=id)
    chapters = Chapter.objects.filter(course=current_course)
    context = {
        "chapters":chapters,
        "course":course,
        "current_course":current_course,
    }
    return render(request,"dashboard/courses.html",context)

@login_required
def chapters(request,cou):
    if not request.user.is_suscribed:
        return redirect('/pricing')
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

