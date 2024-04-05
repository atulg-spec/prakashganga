from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
# from dashboard.views import handlelogin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login",handlelogin,name='handlelogin'),
    # path("login/",handlelogin,name='handlelogin'),
    path('logout', auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/', include('social_django.urls',namespace='social')),
    path('courses/', include('courses.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('', include('dashboard.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
