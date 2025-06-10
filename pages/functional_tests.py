import time
import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append("C:/MyRepos/NSCC_Webucator/TestingGoat")
from test_utils.test_helpers import check_table_for_cell_text


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_home_page_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Home | To-Do", self.browser.title) 


    def test_can_start_to_do_list(self):
        # User visits the home page
        self.browser.get("http://localhost:8000")
        self.assertIn("Home | To-Do", self.browser.title)
        # User sees a header with "To-Do Lists"
        main_header_text = self.browser.find_element(By.ID, "to-do-main-header").text
        self.assertIn("To-Do Lists", main_header_text, 
                      msg="'To-Do Lists' NOT found in the main header's text.")
        # User sees a text input box for entering a new to-do item
        textbox = self.browser.find_element(By.ID, "add-todo-textbox")
        self.assertEqual(textbox.get_attribute("placeholder"), "Enter a to-do item", 
                         msg="'Enter a to-do item' NOT found in the textbox placeholder.")
        # User types a to-do task into the input box: "buy milk"
        textbox.send_keys("buy milk")
        # User submits the form w/ the Enter key
        textbox.send_keys(Keys.ENTER)
        time.sleep(0.5)  # Wait X seconds for the page to update
        # The page updates and shows the new to-do item in a table
        table_id = "todo-tbl" 
        self.browser.find_element(By.ID, table_id)
        check_table_for_cell_text(self, table_id, "buy milk")
        # There should still be a textbox to add another item.
        textbox = self.browser.find_element(By.ID, "add-todo-textbox")
        # # User types another to-do task into the input box: "Use milk to bake cake".
        textbox.send_keys("Use milk to bake cake")
        textbox.send_keys(Keys.ENTER)
        time.sleep(0.5)
        # The page updates again and shows the nwe item in the table.
        check_table_for_cell_text(self, table_id, "Use milk to bake cake")
## END class NewVisitorTest()
        

if(__name__ == "__main__"):
    unittest.main()