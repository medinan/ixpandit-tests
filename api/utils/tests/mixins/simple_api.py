from django.shortcuts import reverse

from utils.tests.mixins.factories import UserFactory


class UserCreatorMixin:
    """
    this class adds the possibility to create a user to be authenticated in the tests
    """

    def create_user(self):
        """
        Create and return a user
        """
        return UserFactory.create()


class BaseSimpleAPITestCaseMixin:
    """
    create and run generic test cases in apis
    """

    factory_class = None
    quantity_entities_to_create = 10
    base_name_api = None

    def setUp(self) -> None:
        # create models instances from factories
        self.entities = self.factory_class.create_batch(
            self.quantity_entities_to_create
        )

    def get_data_to_create_object(self):
        """
        Get data for post method case
        """
        return {}

    def get_data_to_update_object(self):
        """
        Get data for update method case
        """
        return {}

    def case_list(self):
        url = reverse(f"{self.base_name_api}-list")
        response = self.client.get(url)
        return response

    def case_detail(self):
        url = reverse(
            f"{self.base_name_api}-detail", kwargs={"pk": self.entities[0].pk}
        )
        response = self.client.get(url)
        return response

    def case_create(self):
        url = reverse(f"{self.base_name_api}-list")
        data = self.get_data_to_create_object()
        response = self.client.post(url, data=data)
        return response

    def case_update(self):
        url = reverse(
            f"{self.base_name_api}-detail", kwargs={"pk": self.entities[0].pk}
        )
        data = self.get_data_to_update_object()
        response = self.client.patch(url, data)
        return response

    def case_delete(self):
        url = reverse(
            f"{self.base_name_api}-detail", kwargs={"pk": self.entities[0].pk}
        )
        response = self.client.delete(url)
        return response


class SimpleAPITestCaseMixin(UserCreatorMixin, BaseSimpleAPITestCaseMixin):
    authenticate_user = False

    def setUp(self) -> None:
        super(SimpleAPITestCaseMixin, self).setUp()
        self.user = self.create_user()
        if self.authenticate_user:
            self.client.force_authenticate(user=self.user)
