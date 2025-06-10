import time
import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_home_page_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Home | To-Do", self.browser.title) 
        print(f"!!!! OK, 'Home | To-Do' found in title of browser window.")


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
        time.sleep(0.5)  # Wait for the page to update
        # The page updates and shows the new to-do item in a table
        # The table should exist
        table = self.browser.find_element(By.ID, "id_to-do_table")
        buy_milk_tbl_cell = self.browser.find_element(By.ID, "id_table_cell_1")
        # There is still a textbox to add another item.
        # User enters "Use milk to bake cake"
        # The page updates again, and now shows both items on in the table
        use_milk_tbl_cell = self.browser.find_element(By.ID, "id_table_cell_2")
        self.fail("Finish the test!")
        

if(__name__ == "__main__"):
    unittest.main()