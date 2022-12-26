from django import template

register = template.Library()


@register.filter
def add_to_url(a, b):
    return str(a) + '/' + str(b)


@register.filter
def del_first_item(slug_list):
    return slug_list[1:]

