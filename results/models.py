from django.db import models
from subjects.models import StudentClass
from students.models import Student
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import JSONField

# Create your models here.

class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE, verbose_name=_('Select Class'))
    select_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_('Select Student'))
    marks = JSONField(blank=True, verbose_name=_('Marks'))

    def get_absolute_url(self):
        return reverse('results:declare_result')
    def __str__(self):
        return "%s %s-%s" % (self.select_class.class_name, _('Section'), self.select_class.section)
