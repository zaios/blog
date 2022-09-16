from django.shortcuts import render
from django.http import HttpResponse
    
def personal(request):
    # Show Hello World HTML to home page
    html = '<!doctype html><html><head><title> My Blog </title></head><body>這是HTML版本的Hello World!</body></html>'
    return HttpResponse(html, status=200)
# Create your views here.
