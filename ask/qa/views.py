from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def error(request, *args, **kwargs):
	return HttpResponseNotFound(render_to_string('404.html'))
