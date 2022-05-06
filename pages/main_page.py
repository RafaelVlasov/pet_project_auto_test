from .base_page import BasePage
from selenium.webdriver.common.by import By

# создаём класс главной страницы и наследуем его от класса BasePage определённом в файле base_page.py
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
