from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def fun1(request):
    return render(request,'login.htm')