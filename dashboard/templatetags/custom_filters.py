from django import template

register = template.Library()

@register.filter
def remove_email_suffix(email):
    if email.endswith('@gmail.com'):
        email = email[:-10]  # Remove '@gmail.com'
        while email and email[-1].isdigit():
            email = email[:-1]  # Remove trailing digits
    return email.capitalize() 
