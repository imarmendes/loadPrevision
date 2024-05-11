from django.shortcuts import redirect, render
from projects.forms import ProjectForm
from .models import Project

def create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.autor = request.user
            project.save()

            return redirect(f'/loads/?projectId={project.id}') 
    else:
        form = ProjectForm()
    return render(request, 'create.html', {'form': form})


def myProjects(request):
    if request.method == 'GET':
        projects = Project.objects.filter(autor=request.user)
        return render(request, 'myProjects.html', {'projects': projects})

    if request.method == 'POST':
        return redirect('createProject')  
    return render(request, 'myProjects.html')