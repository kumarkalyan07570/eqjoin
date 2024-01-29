from django.shortcuts import render

# Create your views here.

from app.models import *




def eqjoin(request):
    EMPOBJECTS=emp.objects.select_related('deptno').all()
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'eqjoin.html',d)