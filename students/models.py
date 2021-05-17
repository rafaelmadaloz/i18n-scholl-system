from django.db import models
from student_classes.models import StudentClass
from django.urls import reverse
from django.utils.translation import gettext as _
from datetime import date
from decimal import Decimal
# Create your models here.

class Student(models.Model):
    select_gender = (
        ('Male', _('Male')),
        ('Female', _('Female')),
        ('Other', _('Other')),
    )

    student_name = models.CharField(max_length=100, verbose_name=_("Student Name"))
    student_roll = models.IntegerField(unique=True, verbose_name=_("Student Roll"))
    student_email = models.EmailField(verbose_name=_("Student Email"))
    student_gender = models.CharField(max_length=8, choices=select_gender, verbose_name=_("Student Gender"))
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name=_("Student Class"))
    student_date_of_birth = models.DateField(default=date.today(), verbose_name=_("Student Date of Birth"))
    student_reg = models.DateField(auto_now_add=True, auto_now=False, verbose_name=_("Student Registration"))
    student_payment_value = models.DecimalField(max_digits=18, decimal_places=2, default=Decimal('99.90'), verbose_name=_("Student Payment"))

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.student_name