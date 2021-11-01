from rest_framework import serializers

from apps.pokemons.models import (
    Pokemon,
    PokeEvolutions,
    PokeAbilities,
    PokeHeldItems,
    PokeTypes,
)


class EvolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokeEvolutions
        fields = "__all__"


class PokemonAbilitiesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = PokeAbilities
        fields = ("order", "name")

    def get_name(self, obj):
        return obj.ability.name


class PokemonHeldItemsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = PokeHeldItems
        fields = (
            "name",
            "order",
        )

    def get_name(self, obj):
        return obj.heldItem.name


class PokemonTypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = PokeTypes
        fields = (
            "name",
            "order",
        )

    def get_name(self, obj):
        return obj.type.name


class PokemonSerializer(serializers.ModelSerializer):
    evolutions = EvolutionsSerializer(many=True, read_only=True)
    abilities = PokemonAbilitiesSerializer(many=True, read_only=True)
    held_items = PokemonHeldItemsSerializer(many=True, read_only=True)
    types = PokemonTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = "__all__"
