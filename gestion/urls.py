from django.urls import path
from .views import CategoriaApiView, PlatoApiView, PlatoDestroyAPIView, ListarCategoriaApiView


urlpatterns = [
    # cuando se acceda a la ruta /categorias/ se mandara a llamar a la funcionabilidad de nuestro CategoriaApiView
    path('categorias/', CategoriaApiView.as_view()),
    path('platos/', PlatoApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyAPIView.as_view()),
    path('categoria/<int:pk>', ListarCategoriaApiView.as_view())
]