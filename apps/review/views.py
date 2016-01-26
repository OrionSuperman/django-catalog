from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect # inserted this line
from .models import Manufacturer, Product
def index(request):
	context = Product.objects.all()

	mfg = Manufacturer.objects.all()
	print mfg
	for company in mfg:
		print company.name
	return render(request, 'review/index.html',{'context' : context, 'mfg' : mfg}) # updated this line 

def create(request):
	mfg = Manufacturer.objects.get(id=request.POST['manufacturer'])
	review = Product(name = request.POST['name'], price = request.POST['price'], description = request.POST['description'], manufacturer = mfg)
	review.save()

	return redirect('/')

def product(request, idx):
	item = Product.objects.get(id=idx)
	mfg = Manufacturer.objects.all()
	return render(request, 'review/item.html', {'item':item, 'mfg':mfg})

def update(request):
	item = Product.objects.get(id=request.POST['id'])
	item.name = request.POST['name']
	item.manufacturer = Manufacturer.objects.get(id=request.POST['manufacturer'])
	item.price = request.POST['price']
	item.description = request.POST['description']
	item.save()

	return redirect('/product/'+request.POST['id'])


def delete(request, idx):
	item = Product.objects.get(id=idx)
	item.delete()

	return redirect('/')