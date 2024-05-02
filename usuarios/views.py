from django.shortcuts import render, redirect

from usuarios.forms import LoginForm, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth, messages


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_registro'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request, usuario)    #fazendo login
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao efetuar o login")
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            #CAPTURANDO AS INFORMAÇÕES
            nome = form["nome_registro"].value()
            email = form["email_registro"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():     #verificando se ja existe
                messages.error(request, "Usuário já existe, tente outro")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')



    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')