from django.urls import path, include
from rest_framework import routers

from .views import PokemonViewSet

router = routers.SimpleRouter()
router.register(r"pokemons", PokemonViewSet, basename="pokemons")

urlpatterns = [
    path("", include(router.urls)),
]
