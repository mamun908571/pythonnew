from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    title = "this is a demo html"
    name = "Mamun"
    product_name = ['p1','p2','p3']
    data = {"t":title,"name":name,'prod':product_name}
    
    #print("this is root url function")
    return render(request,'portfolio.html',data)


def demo1(request):
    a = 10 
    b = 12
    c = a + b
    #print("this is root url function")
    return HttpResponse(c)