from django.core.management.base import BaseCommand
import requests
import time
import re

from apps.pokemons.models import (
    PokeTypes,
    PokeHeldItems,
    PokeAbilities,
    PokeEvolutions,
    PokeStats,
    Types,
    HeldItems,
    Abilities,
    Pokemon,
)
from apps.pokemons.data_sources.pokeapi import DataSourceCollector

BASE_API = "https://pokeapi.co/api/v2"  # from polls.models import Question as Poll


# https://pokeapi.co/api/v2/generation/1/


def cleanDatabase():
    #  delete all deependent data
    PokeTypes.objects.all().delete()
    PokeHeldItems.objects.all().delete()
    PokeAbilities.objects.all().delete()
    PokeEvolutions.objects.all().delete()
    PokeStats.objects.all().delete()

    # delete all independent data
    Types.objects.all().delete()
    HeldItems.objects.all().delete()
    Abilities.objects.all().delete()
    Pokemon.objects.all().delete()


def getEvolution(id):
    try:
        species = requests.get(f"{BASE_API}/pokemon-species/{id}/")
        species = species.json()
        evol = requests.get(species["evolution_chain"]["url"])
        evol = evol.json()

        chain = []

        chainSpecies = evol["chain"]

        while chainSpecies:
            chain.append(chainSpecies["species"]["name"])
            if chainSpecies["evolves_to"] and len(chainSpecies["evolves_to"]):
                chainSpecies = chainSpecies["evolves_to"][0]
            else:
                chainSpecies = None

        return chain
    except:
        return []


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write(
            "Note! this comand will takes minutes to complete due to pokeapi limitations."
        )
        time.sleep(2)
        # before the proccess started, database should be clean
        self.stdout.write("- Clean all Database")
        cleanDatabase()
        d = DataSourceCollector()
        p = d.collect_data_from_source()
        d.process(p)
