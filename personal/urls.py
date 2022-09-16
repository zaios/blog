from django.urls import path
from personal import views

app_name = 'personal'
urlpatterns = [
    path('', views.personal, name='personal'),
]
