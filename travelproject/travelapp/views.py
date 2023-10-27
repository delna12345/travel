from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from .models import Name
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    na=Name.objects.all()
    return render(request,'index.html',{'result':obj,'res':na})