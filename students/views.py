from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.formats import localize

# Create your views here.


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('Student Creation')
        context['panel_name'] = _('Students')
        context['panel_title'] = _('Create Student')
        return context

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    field_list = [
        _('Student Name'), _('Roll No'), _('Class'), _('Reg Date'), _('Date of birth'), _('Payment')
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = _('Manage Students')
        context['panel_name']   =   _('Students')
        context['panel_title']  =   _('View Students Info')
        context['field_list']   =   self.field_list
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name_suffix = '_form'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('Update Student Info')
        context['panel_name'] = _('Students')
        context['panel_title'] = _('Update Student info')
        return context

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name_suffix = '_delete'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('Student Delete Confirmation')
        context['panel_name'] = _('Students')
        context['panel_title'] = _('Delete Student')
        return context
