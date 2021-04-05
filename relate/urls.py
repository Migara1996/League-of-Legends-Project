from django.urls import path,include

from . import views

urlpatterns=[
    path('com',views.com,name='com')
]