from django.shortcuts import render

def create(request):
    return render(request, 'create.html')


def list(request):
    return render(request, 'list.html')