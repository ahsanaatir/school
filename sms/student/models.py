from __future__ import unicode_literals

from django.db import models

# Create your models here.


# student information
class student_information(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    RELIGION_CHOICE = (
        ('M', 'Muslim'),
        ('N', 'Non-Muslim'),
    )

    student_name = models.CharField(max_length=150)
    student_name_ur = models.CharField(max_length=150)
    student_bform = models.CharField(max_length=15)
    student_dob = models.DateField()
    student_previous_school= models.CharField(max_length=150)
    student_gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    student_religion = models.CharField(max_length=1, choices=RELIGION_CHOICE)
    student_cast = models.CharField(max_length=50)
    student_class = models.CharField(max_length=50)
    created_on = models.DateField()
    #

    def __str__(self):
        return self.student_name

class family_information(models.Model):
    student = models.ForeignKey(student_information)
    father_name = models.CharField(max_length=150)
    father_name_ur = models.CharField(max_length=150)
    father_cnic = models.CharField(max_length=15)

    gurdian_name = models.CharField(max_length=150)
    gurdian_name_ur = models.CharField(max_length=150)
    gurdian_cnic = models.CharField(max_length=15)

    mother_name = models.CharField(max_length=150)
    mother_name_ur = models.CharField(max_length=150)
    mother_cnic = models.CharField(max_length=15)

    father_education = models.CharField(max_length=50)
    father_profession = models.CharField(max_length=50)

    mother_education = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=50)

    father_income = models.IntegerField()
    mother_income = models.IntegerField()

    income_household = models.IntegerField()

    no_of_childern = models.IntegerField()

    brother = models.IntegerField()
    sister = models.IntegerField()

    def __str__(self):
        return self.student.student_name + ' - ' +self.father_name;

class contact_information(models.Model):
    student = models.ForeignKey(student_information)
    permanent_address = models.TextField()
    present_address = models.TextField()
    father_office_address = models.TextField()
    contact_no = models.IntegerField()
    mother_contact_no = models.IntegerField()
    gurdian_contact_no = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.student.student_name

class annual_dues(models.Model):
    student = models.ForeignKey(student_information)
    school_registration_fee = models.IntegerField()
    admission_fee = models.IntegerField()

    annual_paper_fund = models.IntegerField()
    annual_science_fund = models.IntegerField()
    annual_generator_fund = models.IntegerField()
    annual_ice_fund = models.IntegerField()
    class_promotion_fund = models.IntegerField()

    def __str__(self):
        return self.student.student_name + ' - ' + self.school_registration_fee


