from django import template

register = template.Library()


@register.filter
def liked_by(likable_object, user):
    return likable_object.liked_by(user)
