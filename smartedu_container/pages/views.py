from django.shortcuts import render


# #Http methodlarini ekledik
# from django.http import HttpResponse
# def arin(request):
#     return HttpResponse("<h1>Arin</h1>")

def index(request):
    return render(request, 'index.html')     

def about(request):
    return render(request, 'about.html')