import event.static as static

from django import template

from event.models import Event
from django.shortcuts import get_object_or_404

register = template.Library()

@register.inclusion_tag('event/event_attendance.html')
def event_attendence(event_id):
    data = {}
    event = get_object_or_404(Event, id = event_id)
    data['going_attendants'] = event.attendants.filter(attendant__state=static.BK_ATTENDING)
    data['not_going_attendants'] = event.attendants.filter(attendant__state=static.BK_NOT_ATTENDING)
    data['maybe_attendants'] = event.attendants.filter(attendant__state=static.BK_MAYBE_ATTENDING)
    return data