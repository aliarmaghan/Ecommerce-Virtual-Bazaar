from django.shortcuts import render
from ecommerceapp.models import Contact,Product
from django.contrib import messages
from math import ceil




# Create your views here.
def index(request):
    allProds =[]
    catprods = Product.objects.values('category', 'id')
    categ = {items['category'] for items in catprods}
    for cate in categ:
        prod = Product.objects.filter(category = cate)
        n = len(prod)
        nSlides = n // 4 + ceil((n/4)-(n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, "index.html", params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        pnumber = request.POST.get('pnumber')
        myquery = Contact(name=name, email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We will get back to you soon...")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")