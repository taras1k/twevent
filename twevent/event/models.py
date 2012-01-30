# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name = models.CharField('Назва', max_length=200)
    date = models.DateField('Дата')
    address = models.CharField('Адреса', max_length=255, blank=True, null=True)
    attendents = models.ManyToManyField(User)
    description = models.TextField('Опис', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
