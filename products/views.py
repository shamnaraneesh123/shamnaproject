from django.shortcuts import render
from django.http import httpResponse

def ok(request);
      return render(request,'ok.html')
