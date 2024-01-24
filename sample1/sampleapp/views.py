from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

# Create your views here.
def demo(request):
   obj=Place.objects.all()
   return render(request,"index.html",{'result':obj})

# def about(request):
#    return render(request,"about.html")
# def contact(request):
#    return HttpResponse("Hello I am Contact")
# def addition(request):
#    num1=int(request.GET['num1'])
#    num2=int(request.GET['num2'])
#    res=num1+num2
#    return render(request,"result.html",{'res':res})