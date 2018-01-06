# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:29:29 2018

@author: Lenovo
"""
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'current_datetime.html',\
                  {'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render(request,'hours_ahead.html',\
		{'hours_offset':offset,'next_time':dt})
    
def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

