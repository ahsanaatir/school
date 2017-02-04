from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(student_information)
admin.site.register(family_information)
admin.site.register(contact_information)
admin.site.register(annual_dues)