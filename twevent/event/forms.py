# -*- coding: utf-8 -*-
from django import forms
from models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        attendents =  ('content_type','object_pk','slug','pub_date')
    