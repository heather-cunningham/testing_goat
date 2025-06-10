from django.test import TestCase
from django.http import HttpRequest
from pages.views import homepage



class HomePageTest(TestCase):
    ## In fcnal tests:  No need to repeat here.
    # def test_homepage_has_correct_title(self):
    #     request = HttpRequest()
    #     response = homepage(request) 
    #     html = response.content.decode("utf-8")
    #     self.assertIn("<title>Home | To-Do</title>", html)


    def test_empty_url_slug_is_homepage(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/homepage.html")


    def test_homepage_renders_input_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form id="add-todo-item-form" method="POST">')
        self.assertContains(response, '<input id="add-todo-textbox" name="add_todo">')




