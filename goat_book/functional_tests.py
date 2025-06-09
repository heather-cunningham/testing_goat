from selenium import webdriver


browser = webdriver.Firefox()


browser.get("http://localhost:8000")
# Checks for the default Django installation worked page after running the Django dev server
assert "Congratulations!" in browser.title
print("OK")