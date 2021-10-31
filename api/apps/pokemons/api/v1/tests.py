from rest_framework import status
from rest_framework.test import APITestCase

from utils.tests.mixins.factories import UserFactory
from utils.tests.mixins.simple_api import SimpleAPITestCaseMixin

from ...tests.factories import PokemonFactory


class PokemonAnonymousUserAPITestCase(SimpleAPITestCaseMixin, APITestCase):
    factory_class = PokemonFactory
    base_name_api = "pokemons"
    authenticate_user = False

    def test_list(self):
        response = self.case_list()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.case_detail()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        response = self.case_create()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        response = self.case_delete()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        response = self.case_update()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PokemonAuthenticatedUser(SimpleAPITestCaseMixin, APITestCase):
    factory_class = PokemonFactory
    base_name_api = "pokemons"
    authenticate_user = True

    def create_user(self):
        return UserFactory.create()

    def get_data_to_create_object(self):
        return {
            "name": "Picachu", "poke_id": 152,
            "height": 350.00, "weight": 450.77,
            "image": "https://www.imagenes.com/image.png"
        }

    def get_data_to_update_object(self):
        return {"name": "Pikachu"}

    def test_list(self):
        response = self.case_list()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        response = self.case_detail()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        response = self.case_create()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.__dict__)

    def test_delete(self):
        response = self.case_delete()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        response = self.case_update()
        self.assertEqual(response.status_code, status.HTTP_200_OK)