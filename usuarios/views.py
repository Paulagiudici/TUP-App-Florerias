from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages

def registro(request):
    # Si es una solicitud POST (envío del formulario)
    if request.method == 'POST':
        # 1. Asigna los datos POST al formulario de Django
        form = UserCreationForm(request.POST) 
        
        # 2. Usa la validación robusta de Django
        if form.is_valid():
            # Si es válido, crea y guarda el usuario
            form.save() 
            
            # Obtiene el nombre de usuario para el mensaje
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            
            # 3. Redirige al login
            return redirect('usuarios:login')
            # Si es una solicitud GET o si el POST falló la validación
    else:
        # Crea un formulario vacío para mostrar
        form = UserCreationForm()
    
    # Renderiza la plantilla, pasando el objeto 'form' requerido por {{ form.as_p }}
    return render(request, 'usuarios/registro.html', {'form': form})