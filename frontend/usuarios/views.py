from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))  # Redirige al inicio
        else:
            return render(request, '/home/karenarriola/Downloads/Independent/Pizzer-a-/frontend/usuarios/templates/login.html', {'error': 'Credenciales inválidas'})
    return render(request, '/home/karenarriola/Downloads/Independent/Pizzer-a-/frontend/usuarios/templates/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password != cpassword:
            return render(request, '/home/karenarriola/Downloads/Independent/Pizzer-a-/frontend/usuarios/templates/registro.html', {'error': 'Las contraseñas no coinciden'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))  # Redirige al inicio
        else:
            return render(request, '/home/karenarriola/Downloads/Independent/Pizzer-a-/frontend/usuarios/templates/registro.html', {'error': 'Credenciales inválidas'})
    return render(request, '/home/karenarriola/Downloads/Independent/Pizzer-a-/frontend/usuarios/templates/registro.html')
