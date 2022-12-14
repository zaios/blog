"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#https://www.django-rest-framework.org/api-guide/authentication/

from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from personal import views

schema_view = get_schema_view(
   openapi.Info(
      title="blog API",
      default_version='v1',
      description="blog API Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', views.obtain_auth_token), 
    path('admin/', admin.site.urls),
    # path('personal/', include('personal.urls', namespace='personal')),
    path('api/', include('blog.router')),
]
# https://blog.typeart.cc/django%E8%88%87django%20REST%20framework(DRF)%E9%96%8B%E7%99%BC%E7%AD%86%E8%A8%98/