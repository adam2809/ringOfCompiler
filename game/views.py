from django.shortcuts import render
from game.models import Task

def homePage(request):
    print(Task.objects.first().problemName)
    return render(request,'index.htm')


def gamePage(request):
    return render(request,'game.html')
