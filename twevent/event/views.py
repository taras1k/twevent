# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.conf import settings
from forms import EventForm
from models import Event, Atendent
from django.shortcuts import get_object_or_404

ATTENDING = 'yes'
NOT_ATTENDING = 'no'
MAYBE_ATTENDING = 'maybe'
NOT_DECIDED = 'dono'

BK_ATTENDING = 1
BK_NOT_ATTENDING = 0
BK_MAYBE_ATTENDING = 2
BK_NOT_DECIDED = -1


USER_EVENT_ATTENDING = {
                        ATTENDING : 1,
                        NOT_ATTENDING : 0,
                        MAYBE_ATTENDING : 2,
                        NOT_DECIDED : -1,                        
                        }


def _is_attending(user, event_id):
    try:
        attendent_state = Atendent.objects.get(user=user, event__id__exact=event_id)
    except Atendent.DoesNotExist:
        return USER_EVENT_ATTENDING[NOT_DECIDED]
    return attendent_state.state    
    

def default(request):
    data = {}
    data['user'] = request.user
    return render_to_response('event/default.html', data)

@csrf_exempt
@login_required
def create(request):
    data = {}
    data['user'] = request.user
    form = EventForm(request.POST or None)
    data['form'] = form
    if form.is_valid():
        obj = form.save(commit = False) #get an unbound object        
        obj.save()
        return HttpResponseRedirect('/event/%s' % obj.id)     
    return render_to_response('event/create.html', data)

def attending_menu(except_status):
    menu = {
             BK_ATTENDING : {'name' : 'go', 'status' : ATTENDING},
             BK_NOT_ATTENDING : {'name' : 'not go', 'status' : NOT_ATTENDING},
             BK_MAYBE_ATTENDING : {'name' : 'maybe', 'status' : MAYBE_ATTENDING},
            }
    if except_status in menu:
        menu.pop(except_status)
    return menu 
    


def view_event(request, event_id):
    data = {}
    data['user'] = request.user
    event = get_object_or_404(Event, id = event_id)
    data['event'] = event
    if request.user.is_authenticated():
        data['attanding_status'] = _is_attending(request.user, event_id)
    else:
        data['attanding_status'] = USER_EVENT_ATTENDING[NOT_DECIDED]
    data['attending_menu'] = attending_menu(data['attanding_status'])
    return render_to_response('event/view.html', data)
    
@csrf_exempt
@login_required
def attend_event(request,event_id):
    if request.method == 'GET':
        status = request.GET.get('status', None)        
    if status is not None: 
        event = get_object_or_404(Event, id = event_id)
        if USER_EVENT_ATTENDING.get(status, -1) >= 0:
            try:
                attend = Atendent.objects.get(event__id__exact = event_id, user = request.user)
            except Atendent.DoesNotExist: 
                attend = Atendent(event=event, user=request.user)
            attend.state = USER_EVENT_ATTENDING[status]
            attend.save()
    return HttpResponseRedirect('/event/%s' % event_id)
    
            
        
    