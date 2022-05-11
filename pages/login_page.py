from .base_page import BasePage
from .locators import LoginPageLocators

# создаём класс страницы авторизации и наследуем его от класса BasePage определённом в файле base_page.py
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), "Registration link is not presented"
