from django_filters import rest_framework as filters

from apps.pokemons.models import Pokemon


class PokemonFilterSet(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Pokemon
        fields = ("name",)
