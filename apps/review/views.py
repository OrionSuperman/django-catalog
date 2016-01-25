from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect # inserted this line
def index(request):
  return render(request, 'quiz/index.html') # updated this line 

def create(request):
	pass

def product(request):
	pass