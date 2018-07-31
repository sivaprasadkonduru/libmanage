from django import template

register = template.Library()


@register.filter
def book_length(name):
    if len(name) >= 10:
        return name


@register.filter
def num_to_char(char):
    d = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
    return d.get(char, 'Ten')


@register.filter
def book_name(name):
    return name.split()[0]


@register.simple_tag
def my_tag():
    return "#6eacf2"