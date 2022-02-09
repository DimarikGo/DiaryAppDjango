from django import template

from PatDiary.models import WeekDay

register = template.Library()


@register.simple_tag(name="get_patients")
def get_patients():
    return WeekDay.objects.all()



