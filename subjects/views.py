from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from .models import Subject, SubjectCombination
from .forms import SubjectForm, SubjectCombinationForm
from django.urls import reverse_lazy
# Create your views here.



class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('Subject Creation')
        context['panel_name'] = _('Subjects')
        context['panel_title'] = _('Add Subject')
        return context

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    field_list = [
        _('Subject Name'), _('Subject Code'), _('Creation Date'), _('Last Updated')
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = _('Manage Subjects')
        context['panel_name']   =   _('Subjects')
        context['panel_title']  =   _('View Subjects Info')
        context['field_list']   =   self.field_list
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:subject_list')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    template_name_suffix = '_delete'
    success_url = reverse_lazy('subjects:subject_list')

    
    def get_context_data(self, **kwargs):
        context = super(SubjectDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('Subject Delete Confirmation')
        context['panel_name'] = _('Subjects')
        context['panel_title'] = _('Delete Subject')
        return context
    
class SubjectCombinationCreateView(LoginRequiredMixin, CreateView):
    model = SubjectCombination
    form_class = SubjectCombinationForm
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('SubjectCombination Creation')
        context['panel_name'] = _('SubjectConbinations')
        context['panel_title'] = _('Create SubjectConbination')
        return context

class SubjectCombinationListView(LoginRequiredMixin, ListView):
    model = SubjectCombination
    field_list = [
        _('Class'), _('Section'), _('Subject')
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = _('Manage SubjectCombinations')
        context['panel_name']   =   _('SubjectCombinations')
        context['panel_title']  =   _('View SubjectCombinations Info')
        context['field_list']   =   self.field_list
        return context

class SubjectCombinationUpdateView(LoginRequiredMixin, UpdateView):
    model = SubjectCombination
    template_name_suffix = '_form'
    form_class = SubjectCombinationForm
    success_url = reverse_lazy('subjects:subject_combination_list')

class SubjectCombinationDeleteView(LoginRequiredMixin, DeleteView):
    model = SubjectCombination
    template_name_suffix = "_delete"
    success_url = reverse_lazy('subjects:subject_combination_list')

    def get_context_data(self, **kwargs):
        context = super(SubjectCombinationDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = _('SubjectCombination Delete Confirmation')
        context['panel_name'] = _('SubjectCombinations')
        context['panel_title'] = _('Delete SubjectCombination')
        return context
