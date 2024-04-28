from django.shortcuts import render

# Create your views here.
def home(request):
    settings = {}

    currentPath = request.path

    settings['currentPath'] = currentPath

    return render(request, 'home.html', { 'settings': settings })
    
# Create your views here.
def about(request):
    settings = {}
    
    currentPath = request.path

    settings['currentPath'] = currentPath

    return render(request, 'about.html', { 'settings': settings })
    