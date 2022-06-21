from .import views
from django.urls import path
#primera ruta para la aplicacion
urlpatterns = [ 
    path('plantillaejm', views.plantillaejm, name='plantillaejm'),
    path('marca', views.marca, name='marca'),
    path('registro', views.registro,name='registro'),
]

#127.0.0.1:8000/plantillaejm 
#127.0.0.1:8000/marca