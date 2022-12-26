from django.test import TestCase, Client
from django.urls import reverse

from menu.models import MenuElement


class TestMenu(TestCase):

    @classmethod
    def setUpClass(cls):
        """Create nested categories with only one branch for easy operation"""
        super(TestMenu, cls).setUpClass()
        first = MenuElement.objects.create(name='firth', slug='first',
                                           parent=None)
        second = MenuElement.objects.create(name='second', slug='second',
                                            parent=None)
        third = MenuElement.objects.create(name='third', slug='third',
                                           parent=first)
        fourth = MenuElement.objects.create(name='fourth', slug='fourth',
                                            parent=first)
        fifth = MenuElement.objects.create(name='fifth', slug='fifth',
                                           parent=third)
        sixth = MenuElement.objects.create(name='sixth', slug='sixth',
                                           parent=third)
        seventh = MenuElement.objects.create(name='seventh', slug='seventh',
                                             parent=fifth)
        eighth = MenuElement.objects.create(name='eighth', slug='eighth',
                                            parent=fifth)
        ninth = MenuElement.objects.create(name='ninth', slug='ninth',
                                           parent=fifth)

    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        """Check if all root categories listed in main page"""
        request = self.client.get(reverse('main'))
        assert request.status_code == 200
        body = request.content.decode()
        root_categories = MenuElement.objects.filter(parent=None)
        for category in root_categories:
            assert category.name in body

    def test_recursive_adding_menu_row(self):
        """
        All categories should be listed when we chose last parent category
        in our single branch
        """
        request = self.client.get(
            'http://127.0.0.1:8000/query/first/third/fifth/')
        assert request.status_code == 200
        body = request.content.decode()
        elements = MenuElement.objects.all()
        for element in elements:
            assert element.name in body

    def test_db_models_correct_work(self):
        """
        Testing correct relation work

        This test should be separate, but in this class data is prepared and
        testing functional is not so big
        """

        root_categories = MenuElement.objects.filter(parent=None)
        assert len(root_categories) == 2
        fifth = MenuElement.objects.get(name='fifth')
        children = fifth.children.all()
        assert len(children) == 3
