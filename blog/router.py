from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from personal import views
from rest_framework.authtoken import views
from rest_framework import routers
from personal.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register('userprofile', UserProfileViewSet) 

urlpatterns = [
	url(r'^', include(router.urls)),
]