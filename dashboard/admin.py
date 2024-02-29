from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'is_suscribed', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('suscribed_date','expiry_date')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Suscription Details', {'fields': ('is_suscribed',)}),
        ('Important dates', {'fields': ('suscribed_date','expiry_date','last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        return formfield

# Register the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)


from social_django.models import Nonce,UserSocialAuth,Association
from social_django.admin import Nonce,UserSocialAuth,Association
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.unregister(Association)


# ----------Admin Customization------------
admin.site.site_header = "Prakash Ganga Admin"
admin.site.site_title = "Prakash Ganga Capitals"
admin.site.index_title = " | Admin"
admin.site.unregister(Group)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Chapter)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('chapter_number','chapter_name','course','date_time')
    list_filter = ('date_time','course')

