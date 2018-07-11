# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "surveyform/index.html")

def process_form(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries']=0
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    request.session['tries']+=1
    return redirect('/result')

def display_result(request):
    return render(request, "surveyform/result.html")

def reset(request):
    del request.session['tries']
    return redirect('/')
