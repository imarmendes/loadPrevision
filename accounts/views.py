from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re

def register(request):
    if request.method == 'POST':
        # Recebendo os dados do formulário
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Verificando se as senhas coincidem
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')  # Redirecionando de volta para a página de registro

        # Verificando o formato do e-mail usando regex
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.error(request, 'Por favor, insira um endereço de e-mail válido.')
            return redirect('register')  # Redirecionando de volta para a página de registro

        # Verificando se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
            return redirect('register')  # Redirecionando de volta para a página de registro

        # Verificando se o email já está em uso
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este endereço de e-mail já está em uso.')
            return redirect('register')  # Redirecionando de volta para a página de registro

        # Criando o novo usuário se todas as validações passaram
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, 'Usuário criado com sucesso. Faça login para acessar a plataforma.')
        return redirect('login')  # Redirecionando para a página de login após o registro

    # Se o método da requisição não for POST, renderiza o formulário de registro
    return render(request, 'registration/register.html')
