from django.test import TestCase
from django.http import HttpRequest
from pages.views import homepage



class HomePageTest(TestCase):
    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request) 
        html = response.content.decode("utf-8")
        #
        #
        self.assertIn("<title>Home | To-Do</title>", html)




