from django.urls import path, include
from auth.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls'))
]
