from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def fun1(request):
        return render(request,'login.htm')

def fun2(request):
        return render(request,'fblogin.htm')

def fun3(request):
        return render(request,'javascript.htm')

def fun4(request):
        return render(request,'calculater.htm')