import locale
from django import forms
from students.models import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.utils.translation import to_locale, get_language

class StudentForm(forms.ModelForm):
    locale_symbol = to_locale(get_language())
    locale.setlocale(locale.LC_ALL, locale_symbol+'.UTF-8')
    symbol_payment = locale.localeconv()
    student_payment_value = forms.DecimalField(localize=True, label=(f"{_('Student Payment')} ({symbol_payment['int_curr_symbol']} - {symbol_payment['currency_symbol']})"), widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['student_reg']
        widgets = {
            'student_name'  :   forms.TextInput(attrs={'class':'form-control'}),
            'student_roll'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'student_email'  :   forms.EmailInput(attrs={'class':'form-control'}),
            'student_gender'  :   forms.Select(attrs={'class':'form-control'}),
            'student_class'  :   forms.Select(attrs={'class':'form-control'}),
            'student_date_of_birth'  :   forms.DateInput(attrs={'class':'form-control'}),
        }