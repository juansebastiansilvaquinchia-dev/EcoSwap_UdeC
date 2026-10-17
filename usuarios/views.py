from django.shortcuts import render, redirect

def iniciar_sesion(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        # Simulacion de autenticación (en un caso real, deberías verificar la contraseña y la existencia del usuario)
        if email:  # Verifica si el email existe (simulación)
            request.session["usuario_email"] = email
            return redirect("perfil_usuario")
    return render(request, "usuarios/login.html")


def perfil_usuario(request):
    email = request.session.get("usuario_email", "estudiante@universidad.edu")
    context = {
        "email": email,
        "nombre": email.split('@')[0].replace('.', ' ').title(),
    }
    return render(request, "usuarios/perfil.html", context)

def cerrar_sesion(request):
    if "usuario_email" in request.session:
        del request.session["usuario_email"]
    return redirect("iniciar_sesion")