from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import math

def predict(request):
    return render(request, 'predict.html',{'name':'migara'})


def add(request):

    v1=float(request.GET['num1'])
    v2=int(request.GET['num2'])

    v6=float(request.GET['num6'])
    v7=int(request.GET['num7'])
 
    
    res=1/(1+math.exp((-1)*(-3.16680195e-16-7.3911925e-12*v6+6.90445856e-12*v1-4.64926719e-11*v7+4.09707292e-11*v2-1.97884206e-07*v6*v7+1.97956900e-07*v1*v2)))

    if(res>0.5):
        p=['Blue Team Wins',round(res,3)]
    else:
        p=['Red Team Wins',1-round(res,3)]

    return render(request, 'result.html',{'result':p})
    
