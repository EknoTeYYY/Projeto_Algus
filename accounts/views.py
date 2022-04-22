from pyexpat.errors import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        check = auth.authenticate(request, username=user, password=password)

        if check is not None:
            login(request, check)

            if check.is_superuser:

                return redirect('cad')

            else:
                return redirect('produto')
        else:
            messages.info(request, 'Usuário ou senha invalida.')
            return render(request, 'paginas/login.html')

    else:
        return render(request, 'paginas/login.html')


def cadastrar(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordconfirmation = request.POST.get('password2')
        if password != passwordconfirmation:
            return render(request, 'paginas/cadastro.html')

        add=User.objects.create_user(username=user, email=email, password=password)
        add.save()

        return redirect('cad')

    else:
        return render(request, 'paginas/cadastro.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def redefinir(request):
    if request.method == 'POST':
        id = request.user.id
        usuario = User.objects.get(id=id)
        usuario.set_password(request.POST.get('pass'))
        usuario.save()
        if usuario:
            messages.info(request, 'Senha redefinida com sucesso.')
            return redirect('home')
    else:
        return render(request, 'paginas/redefinir.html')

