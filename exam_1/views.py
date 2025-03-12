from django.http import HttpResponse
from django.shortcuts import render, redirect

def error(request):
    # return HttpResponse("Неверный путь")
    return render(request, "index.html")