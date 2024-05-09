"""
URL configuration for portalinmobiliario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import registro_usuario,index, detalle_inmueble, crear_solicitud_arriendo, success, mi_perfil, obtener_comunas,iniciar_sesion
0
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from portalinmobiliario import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('registro/', registro_usuario, name='registro_usuario'),
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('detalle_inmueble/<int:id>/', detalle_inmueble, name='detalle_inmueble'),
    path('crear_solicitud/<int:inmueble_id>/', crear_solicitud_arriendo, name='crear_solicitud_arriendo'),
    path('success/', success, name="success"),
    path('mi_perfil/', mi_perfil, name="mi_perfil"),
    path('obtener_comunas/', obtener_comunas, name='obtener_comunas'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
