from django.urls import path
from dashboard.views import *
from django.contrib.auth import views as auth_views
# urls.py
urlpatterns = [
    # PAGES
    path("",home,name='home'),
    path("about",about,name='about'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("opendemat",opendemat,name='opendemat'),
    path("contactus",contact,name='contactus'),
    path("pricing",pricing,name='pricing'),
    path("payment_status",payment_status,name='payment_status'),
    path("investment",investment,name='investment'),
    path("careers",careers,name='careers'),
    # POLICY
    path("termsofuse",termsofuse,name='termsofuse'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("privacypolicy",privacypolicy,name='privacypolicy'),
    path("refundpolicy",refundpolicy,name='refundpolicy'),
    # DASHBOARD
    path("course",course,name='course'),
    path("courses/<str:id>",courses,name='courses'),
    path("chapters/<str:cou>",chapters,name='chapters'),
]
