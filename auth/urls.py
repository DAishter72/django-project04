from django.urls import path, include
from django.contrib.auth import views as auth_views
from auth.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Opcional: recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
]
