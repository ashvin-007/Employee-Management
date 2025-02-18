from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Emp(models.Model):
    emp_name=models.CharField( max_length=100)
    emp_id=models.IntegerField()
    emp_phone=models.CharField(max_length=100)
    emp_address=models.CharField(max_length=200)
    emp_is_active=models.BooleanField(default=False)
    emp_department=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} {self.emp_name} {self.emp_id} {self.emp_phone} {self.emp_address} {self.emp_is_active} {self.emp_department} "
    
class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='picture')
    testimonial=models.TextField()
    rating=models.IntegerField(  validators=[MinValueValidator(1), MaxValueValidator(5)])
    