from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import index

class HomeTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)
