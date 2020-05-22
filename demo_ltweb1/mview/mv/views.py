from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'mv/home.html')


def base(request):
    return render(request, 'mv/base.html')

def listMv(request):
    return render(request, 'mv/list-mv.html')

def detailMV(request):
    return render(request, 'mv/detail-mv.html')
