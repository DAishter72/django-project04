from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Este correo electrónico ya está registrado.")
        return email


class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm  # Usamos nuestro formulario personalizado
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # Guardar el usuario primero
        response = super().form_valid(form)

        # Autenticar y loguear al usuario automáticamente después del registro
        user = form.save()
        login(self.request, user)

        # Mensaje de éxito
        messages.success(
            self.request,
            f'¡Registro exitoso! Bienvenido {user.username}.'
        )

        return response

    def form_invalid(self, form):
        # Manejar errores de formulario con mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(
                    self.request,
                    f"Error en {field}: {error}"
                )
        return super().form_invalid(form)
