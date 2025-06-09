import unittest 
from selenium import webdriver


class NewDjangoProjectTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_django_installed_correctly(self):
        self.browser.get("http://localhost:8000")
        # Checks for the default Django installation worked page after running the Django dev server
        # assert "Congratulations!" in self.browser.title, f"Browser title found: {self.browser.title}"
        self.assertIn("Congratulations!", self.browser.title) # Does same as above, but output a little cleaner
        print(f"!!!! OK, 'Congratulations' found in title of browser window.\n"
              f"!!!! If you're seeing this message, Django installed successfully.")
        

if(__name__ == "__main__"):
    unittest.main()






