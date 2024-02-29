from django.urls import path
from dashboard.views import *
from django.contrib.auth import views as auth_views
# urls.py
urlpatterns = [
    # PAGES
    path("",home,name='home'),
    path("about",about,name='about'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("contact",contact,name='contact'),
    path("pricing",pricing,name='pricing'),
    # POLICY
    path("termsconditions",termsconditions,name='termsconditions'),
    path("disclaimer",disclaimer,name='disclaimer'),
    path("privacypolicy",privacypolicy,name='privacypolicy'),
    path("refundpolicy",refundpolicy,name='refundpolicy'),
    # DASHBOARD
    path("dashboard",dashboard,name='dashboard'),
    path("course",course,name='course'),
    path("courses/<str:id>",courses,name='courses'),
    path("chapters/<str:cou>",chapters,name='chapters'),
]
