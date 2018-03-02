from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

# Create your views here.
def index(request):
	return HttpResponse('<html><body>Hello World!</body></html>')

def about(request):
	return HttpResponse("This is the about page. <a href='/'>Back Home</a>")

def better(request):
	t = loader.get_template('betterhello.html')
	c = {'current_time': datetime.now(), }
	return HttpResponse(t.render(c))
