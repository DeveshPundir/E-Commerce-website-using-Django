from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Contact
from math import ceil
def index(request):
  
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nslides),nslides])
  
    return render (request,'shop/index.html',{'allProds':allProds})
def about(request):
    return render (request,'shop/about.html')
def contact(request):
    
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    phone=request.POST.get('phone','')
    desc=request.POST.get('desc','')
    contact=Contact(name=name,email=email,phone=phone,desc=desc)
    contact.save()
    return render (request,'shop/contact.html')
def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    return False
def search(request):
    query=request.GET.get('search')
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods }
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        if len(prod)!= 0 :
          allProds.append([prod,range(1,nslides),nslides])
    return render (request,'shop/index.html',{'allProds':allProds})
def productview(request,myid):
    # Fetch the product usiong the id
    product=Product.objects.filter(id=myid)
    
    return render (request,'shop/productview.html',{'product':product[0]})
def checkout(request):
    return render (request,'shop/checkout.html')

# Create your views here.
