from django.urls import path
from arriendos import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('solicitud/<int:inmueble_id>', views.nuevaSolicitud , name='solicitud'),
    path('solicitud/exito', views.exito , name='exito_solicitud'),
    path('usuario/update/', views.userUpdate , name='update_usuario'),
    path('arrendador/', views.arrendador , name='arrendador'),
    path('arrendatario/', views.arrendatario , name='arrendatario'),

]
