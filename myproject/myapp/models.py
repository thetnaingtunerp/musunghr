from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name
    
class position(models.Model):
    position = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position


class marital(models.Model):
    status = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class gender(models.Model):
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.gender
    
class type(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status
    
class edu_grade(models.Model):
    grade = models.CharField(max_length=225)

    def __str__(self):
        return self.grade

class state_region(models.Model):
    state_name = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.state_name
    
class township(models.Model):
    township = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.township


class employee_profile(models.Model):
    employee_id = models.CharField(max_length=225, unique=True)
    contract_id = models.CharField(max_length=225)
    finger_id = models.CharField(max_length=225,blank=True, null=True)
    employee_name = models.CharField(max_length=225, blank=True, null=True)
    ssb_id = models.CharField(max_length=225, blank=True, null=True)
    nrc_no = models.CharField(max_length=225, unique=True)
    fathername = models.CharField(max_length=225)
    mothername = models.CharField(max_length=225)
    gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    race = models.CharField(max_length=225, blank=True, null=True)
    religion = models.CharField(max_length=225, blank=True, null=True)
    dob = models.DateField()
    marital = models.ForeignKey(marital, on_delete=models.CASCADE)
    entrydate = models.DateField()
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    position = models.ForeignKey(position, on_delete=models.CASCADE)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    education = models.ForeignKey(edu_grade, on_delete=models.CASCADE)
    phone = models.CharField(max_length=225, blank=True, null=True)
    address = models.TextField() 
    township = models.ForeignKey(township, on_delete=models.CASCADE)
    district = models.CharField(max_length=225, blank=True, null=True)
    state_region = models.ForeignKey(state_region, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='', blank=True, null=True)
    familytable = models.ImageField(upload_to='', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_name


class education_profile(models.Model):
    employee_name = models.ForeignKey(employee_profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=225)
    education_level = models.CharField(max_length=225)
    from_date = models.DateField()
    to_date = models.DateField()


class work_exp(models.Model):
    employee_name = models.ForeignKey(employee_profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=225)
    position = models.CharField(max_length=225)
    from_date = models.DateField()
    to_date = models.DateField()


