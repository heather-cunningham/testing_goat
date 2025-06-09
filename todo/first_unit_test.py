import unittest 
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_can_start_to_do_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title) 
        print(f"!!!! OK, 'To-Do' found in title of browser window.")
        

if(__name__ == "__main__"):
    unittest.main()