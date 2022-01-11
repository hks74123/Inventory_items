from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from hks.models import Product
import os
import csv
# Create your views here.
def home(request):
    all_items=reversed(Product.objects.all())
    return render(request,'index.html',{'itms':all_items})

def addpro(request):
    return render(request,'addpro.html')

def edititem(request):
    return render(request,'idform.html')

def additem(request):
    if request.method=='POST':
        pos=Product()
        pos.Product_name=request.POST.get('nameofpro')
        if len(request.FILES)!=0:
            pos.Product_image=request.FILES['imgle']
        pos.Product_category=request.POST.get('catofpro') 
        pos.Product_price=request.POST.get('priceofpro')
        pos.Product_qty=request.POST.get('qtyofpro')
        pos.Product_desc=request.POST.get('desofpro')
        pos.Product_brand=request.POST.get('brandofpro')
        pos.Product_color=request.POST.get('colorofpro')
        pos.Product_size=request.POST.get('sizeofpro')
        pos.Product_store=request.POST.get('storeofpro')
        if(pos.Product_name=='' or pos.Product_category=='' or pos.Product_price=='' or pos.Product_qty=='' or pos.Product_brand==''):
            messages.info(request,'Please fill out * mark field')
            return redirect('/Addproduct')
        pos.save()
        return redirect('/')
    return redirect('/')

def edititemm(request):
    if request.method=='POST':
        getdd=request.POST.get('iddd')
        if 'editt' in request.POST:
            gtobj=Product.objects.filter(id=getdd)
            if(len(gtobj)!=0):
                pid='hks'+getdd
                return render(request,'editthem.html',{'psts':gtobj,'pid':pid})
            else:
                messages.info(request,"Please enter the correct product id")
                return redirect('/editproduct')
        elif 'dlett' in request.POST:
            Product.objects.filter(id=getdd).delete()
            return redirect('/')

def edittheme(request,pid):
    if request.method=='POST':
        getdd=pid[3:]
        pos=Product.objects.get(id=getdd)
        pos.Product_name=request.POST.get('nameofpro')
        if len(request.FILES)!=0:
            if len(pos.Product_image)>0:
                os.remove(pos.Product_image.path)
            pos.Product_image=request.FILES['imgp']
        pos.Product_category=request.POST.get('catofpro') 
        pos.Product_price=request.POST.get('priceofpro')
        pos.Product_qty=request.POST.get('qtyofpro')
        pos.Product_desc=request.POST.get('desofpro')
        pos.Product_brand=request.POST.get('brandofpro')
        pos.Product_color=request.POST.get('colorofpro')
        pos.Product_size=request.POST.get('sizeofpro')
        pos.Product_store=request.POST.get('storeofpro')
        if(pos.Product_name=='' or pos.Product_category=='' or pos.Product_price=='' or pos.Product_qty=='' or pos.Product_brand==''):
            messages.info(request,'Please do not leave * mark field empty')
            gtobj=Product.objects.filter(id=getdd)
            if(len(gtobj)!=0):
                pid='hks'+getdd
                return render(request,'editthem.html',{'psts':gtobj,'pid':pid})
        pos.save()
        return redirect('/')
    return redirect('/')

def getfile(request):
    if request.method=='POST':
        getdd=request.POST.get('pidd')
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="file.csv"'  
        prod = Product.objects.filter(id=getdd)
        writer = csv.writer(response)  
        for p in prod:
            writer.writerow(['Product_id','Product_image_url','Product_price','Product_qty','Product_desc','Product_brand','Product_color','Product_size','Product_category','Product_store'])
            writer.writerow([p.id,p.Product_image,p.Product_name,p.Product_price,p.Product_qty,p.Product_desc,p.Product_brand,p.Product_color,p.Product_size,p.Product_size,p.Product_category,p.Product_store])  
        return response