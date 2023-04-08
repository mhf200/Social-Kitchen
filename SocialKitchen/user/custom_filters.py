from django import template

register = template.Library()

@register.filter(name='stars')
def stars(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return ''
    full_stars = '★' * value
    empty_stars = '☆' * (5 - value)
    return f'{full_stars}{empty_stars}'
