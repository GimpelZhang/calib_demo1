# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
    context          = {}
    context['page1'] = 'Hello World!'
    return render(request, 'page1.html', context)
