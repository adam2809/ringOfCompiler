from django.shortcuts import render

def homePage(request):
    return render(request,'home.html')


def gamePage(request):
    pass
