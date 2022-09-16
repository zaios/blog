from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from personal.models import UserProfile
from personal.serializers import UserProfileSerializer

def personal(request):
    # Show Hello World HTML to home page
    html = '<!doctype html><html><head><title> My Blog </title></head><body>這是HTML版本的Hello World!</body></html>'
    return HttpResponse(html, status=200)
# Create your views here.

class UserProfileViewSet(ModelViewSet):
  	"""
    Suuport User's personal profile
    """
  	serializer_class = UserProfileSerializer
  	queryset = UserProfile.objects.all()
