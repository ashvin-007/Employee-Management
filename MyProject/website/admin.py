from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_name', 'emp_id', 'emp_phone', 'emp_address', 'emp_is_active', 'emp_department')
    search_fields = ('emp_name', 'emp_id')  
    list_filter = ('emp_is_active', 'emp_department') 

admin.site.register(Emp,EmployeeAdmin)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=('id','name','photo','testimonial','rating')
    
admin.site.register(Testimonial,TestimonialAdmin)