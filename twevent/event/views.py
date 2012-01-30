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
from models import Event
from django.shortcuts import get_object_or_404

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

def view_event(request, event_id):
    data = {}
    data['user'] = request.user
    event = get_object_or_404(Event, id = event_id)
    data['event'] = event
    return render_to_response('event/view.html', data)
    
        