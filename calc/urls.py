from django.urls import path,include

from . import views

urlpatterns=[
    path('predict',views.predict,name='predict'),
    path('add',views.add,name='add')
]