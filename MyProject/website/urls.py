from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('emp/home/', home,name='home'),
    path('emp/add_emp/', add_emp,name='add_emp'),
    path('emp/del_emp/<int:id>', del_emp,name='del'),
    path('emp/update_emp/<int:id>', update_emp,name='update'),
    path('emp/testimonial/', testimonial,name='testimonial'),
    path('emp/register/', register,name='register'),
    path('emp/loggedin/', loggedin,name='loggedin'),
    path('emp/loggedout/', loggedout,name='loggedout'),
]
