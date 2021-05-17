from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.

class StudentClass(models.Model):
    class_name              =   models.CharField(max_length=100, help_text=_('Eg- Third, Fouth,Sixth etc'), verbose_name=_("Class Name"))
    class_name_in_numeric   =   models.IntegerField(help_text=_('Eg- 1,2,4,5 etc'), verbose_name=_("Class Name In Numeric")) 
    section                 =   models.CharField(max_length=10, help_text=_('Eg- A,B,C etc'), verbose_name=_("Section"))
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_("Creation Date"))

    def get_absolute_url(self):
        return reverse('student_classes:class_list')

    def __str__(self):
        return "%s %s-%s"%(self.class_name, _("Section"), self.section)
