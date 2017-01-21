from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

import re
register = template.Library()


@register.filter()
def make_link(value, arg=14):
    value = conditional_escape(value)
    output = ''
    for i in value.split(' '):
        if i.startswith(('http://', 'www.', 'https://')):
            output += '<a href="{href}"><span style="color:#3F5600; font-size:{ts}px;">link</span></a> '.format(href=i, ts=arg)
        else:
            output += i + ' '
    return mark_safe(output)
