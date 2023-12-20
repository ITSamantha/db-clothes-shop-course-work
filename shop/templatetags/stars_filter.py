from django import template

register = template.Library()


@register.filter(name='stars')
def stars(value):
    full_stars = int(value)
    half_star = 1 if value - int(value) >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star

    html = '<i class="fas fa-star"></i>' * full_stars
    html += '<i class="fas fa-star-half-alt"></i>' * half_star
    html += '<i class="far fa-star"></i>' * empty_stars

    return html
