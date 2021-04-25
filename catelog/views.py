
#from django.http import HttpResponse,HttpResponseRedirect 
#from django.shortcuts import render, redirect 
#from .forms import *
#from django.views.generic.list import ListView

  
 
#def create(request):
    #create = None
    #if request.method == 'POST':
        #product_form = productForm(request.POST)
        
        #if product_form.is_valid():
        	#product = product_form.save()
        #return HttpResponseRedirect('/')

    #else:
    	#product_form = productForm()

    #return render(request,'catelog/product_form.html',{'product_form': product_form})


#class categoryListView(ListView):
	#template_name = "catelog/product.html"
	#queryset = Product.objects.all()