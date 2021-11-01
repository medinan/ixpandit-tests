from typing import Generator

import requests

from apps.pokemons.data_sources.data_models import (
    PokemonModel,
    EvolutionModel,
    HeldItemsModel,
    AbilitiesModel,
    TypesModel,
    StatModel,
)
from apps.pokemons.models import (
    Pokemon,
    Types,
    PokeTypes,
    PokeHeldItems,
    HeldItems,
    PokeAbilities,
    Abilities,
    PokeEvolutions,
    PokeStats,
)


class DataSourceCollector:
    base_api = "https://pokeapi.co/api/v2"

    def __init__(self):
        self.client = requests.Session()

    def process(self, pokemon_list):
        for poke in pokemon_list:
            print(f"procesando el pokemon {poke.name}")
            obj, _ = Pokemon.objects.update_or_create(
                poke_id=poke.poke_id,
                defaults={
                    "name": poke.name,
                    "height": poke.height,
                    "weight": poke.weight,
                    "image": poke.image,
                },
            )

            for idx, _types in enumerate(poke.types, 1):
                PokeTypes.objects.get_or_create(
                    pokemon=obj,
                    type=Types.objects.get_or_create(name=_types.name)[0],
                    order=idx,
                )

            for idx, _held in enumerate(poke.held_items, 1):
                PokeHeldItems.objects.get_or_create(
                    pokemon=obj,
                    heldItem=HeldItems.objects.get_or_create(name=_held.name)[0],
                    order=idx,
                )

            for idx, _ability in enumerate(poke.abilities, 1):
                PokeAbilities.objects.get_or_create(
                    pokemon=obj,
                    ability=Abilities.objects.get_or_create(name=_ability.name)[0],
                    order=idx,
                )

            for idx, _evolution in enumerate(poke.evolutions):
                PokeEvolutions.objects.update_or_create(
                    pokemon=obj, name=_ability.name, defaults={"order": idx}
                )

            for idx, _stats in enumerate(poke.stats, 1):
                PokeStats.objects.update_or_create(
                    pokemon=obj,
                    name=poke.name,
                    defaults={
                        "effort": _stats.effort,
                        "base_stat": _stats.base_stat,
                    },
                )

    def collect_data_from_source(self):
        get_pokemon_by_generation_response = self.client.get(
            f"{self.base_api}/generation/1/"
        )
        get_pokemon_by_generation_response.raise_for_status()
        list_pokemon_species = get_pokemon_by_generation_response.json()[
            "pokemon_species"
        ]
        for poke in list_pokemon_species:
            pokemon_id = poke["name"]
            pokemon_info_response = requests.get(
                f"{self.base_api}/pokemon/{pokemon_id}/"
            )
            pokemon_info_response.raise_for_status()
            pokemon_info = pokemon_info_response.json()
            pokemon_models = PokemonModel(
                poke_id=pokemon_info["id"],
                name=pokemon_info["name"],
                height=pokemon_info["height"],
                weight=pokemon_info["weight"],
                image=pokemon_info["sprites"]["front_default"],
                evolutions=self.get_evolution(pokemon_id),
                held_items=self.get_held_items(pokemon_info),
                abilities=self.get_abilities(pokemon_info),
                types=self.get_types(pokemon_info),
                stats=self.get_stats(pokemon_info),
            )
            yield pokemon_models

    def get_held_items(self, pokemon_detail):
        return [
            HeldItemsModel(name=it["item"]["name"])
            for it in pokemon_detail["held_items"]
        ]

    def get_abilities(self, pokemon_detail):
        return [
            AbilitiesModel(name=it["ability"]["name"])
            for it in pokemon_detail["abilities"]
        ]

    def get_types(self, pokemon_detail):
        return [TypesModel(name=it["type"]["name"]) for it in pokemon_detail["types"]]

    def get_stats(self, pokemon_detail):
        return [
            StatModel(
                name=it["stat"]["name"], base_stat=it["base_stat"], effort=it["effort"]
            )
            for it in pokemon_detail["stats"]
        ]

    def get_evolution(self, pokemon_id):
        species_response = self.client.get(
            f"{self.base_api}/pokemon-species/{pokemon_id}/"
        )
        species_response.raise_for_status()
        species_info = species_response.json()
        evolution_response = self.client.get(species_info["evolution_chain"]["url"])
        evolution_response.raise_for_status()
        evolution_info = evolution_response.json()
        chain = []
        chain_species = evolution_info["chain"]
        while chain_species:
            chain.append(chain_species["species"]["name"])
            if chain_species["evolves_to"] and len(chain_species["evolves_to"]):
                chain_species = chain_species["evolves_to"][0]
            else:
                chain_species = None
        return [
            EvolutionModel(order=idx, name=name) for idx, name in enumerate(chain, 1)
        ]
