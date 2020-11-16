from django.shortcuts import render
from .models import Inventory
from .forms import InventoryAddForm
from django.shortcuts import redirect

# Create your views here.
def home_view(request):
	return render(request, 'index.html',{})

def showitems_view(request):

	obj = Inventory.objects.all()
	context ={
		'object': obj
	}

	return render(request, 'showitems.html', context)

def edititem(request, id):
	obj = Inventory.objects.get(id=id)
	form = InventoryAddForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('/showitems/')
	context = {
		'form': form
	}
	return render(request, 'additems.html', context)

def delitems(request, id):
	Inventory.objects.filter(id=id).delete()
	return redirect('/showitems/')

def additems_view(request):

	form = InventoryAddForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = InventoryAddForm()

	context = {
		'form': form
	}
	return render(request, 'additems.html',context)


# def additems_view(request):

# 	form = InventoryAddForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = InventoryAddForm()

# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'additems.html',context)
