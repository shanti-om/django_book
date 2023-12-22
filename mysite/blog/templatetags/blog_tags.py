from django import template
import blog.views as views

register = template.Library()


@register.simple_tag()
def det_menu():
    return views.data['menu']

@register.inclusion_tag('blog/header.html')
def show_header(selected=0):
    menu = views.data['menu']
    return {'menu': menu, 'selected': selected}


