from django.shortcuts import render
from division.models import Divisions
# Create your views here.



# def index (request):
#     #return render (request,'admin/division.html')
#     return render (request,'admin/district.html')

def index (request):
    data = Divisions.objects.all()
    data_context={'d':data}
    #return render (request,'admin/division.html')
    return render (request,'admin/district.html',data_context)