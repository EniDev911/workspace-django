from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', LoginView.as_view(), name='login_url'),
    path('register/', views.register_view, name='register_url'),
    path('juego/', views.juego_view, name='juego_url'),
    path('preguntas/', views.preguntas_view, name='preguntas_url'),
    path('preguntas/crear', views.crear_pregunta_view, name='crear_pregunta_url'),
    path('preguntas/<int:id>/eliminar', views.eliminar_pregunta_view, name='eliminar_pregunta_url'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria_url'),
]