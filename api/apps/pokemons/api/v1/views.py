from rest_framework import viewsets, permissions

from apps.pokemons.api.v1.serializers import PokemonSerializer
from apps.pokemons.models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


