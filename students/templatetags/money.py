from django import template
from django import utils
from django.utils.translation import to_locale, get_language
import locale


register = template.Library()

@register.filter
def money(value):
    locale_symbol = to_locale(get_language())
    locale.setlocale(locale.LC_ALL, locale_symbol+'.UTF-8')
    value = locale.currency(value, grouping=True, symbol=True)
    return value