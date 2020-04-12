from django import template

register = template.Library()

def cut(value, arg):
    """
    This cut out values of learning_templates
    """
    return value.replace(arg,'')


register.filter('cut',cut)
