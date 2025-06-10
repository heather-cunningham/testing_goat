from selenium.webdriver.common.by import By

def check_table_for_cell_text(self, tbl_id, tbl_cell_text):
        table = self.browser.find_element(By.ID, tbl_id)
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(tbl_cell_text, [row.text for row in rows])