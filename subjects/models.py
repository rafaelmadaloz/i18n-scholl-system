from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from student_classes.models import StudentClass



# Create your models here.

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, verbose_name=_("Subject Name"))
    subject_code = models.IntegerField(verbose_name=_("Subject Code"))
    subject_creation_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_("Subject Creation Date"))
    subject_update_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=_("Subject Update Date"))

    def __str__(self):
        return self.subject_name
    
    def get_absolute_url(self):
        return reverse('subjects:subject_list')



class SubjectCombination(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name=_("Select Class"))
    select_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Select Subject"))

    def get_absolute_url(self):
        return reverse('subjects:subject_combination_list')

    def __str__(self):
        return '%s %s-%s'%(self.select_class.class_name, _("Section"), self.select_class.section)
    
