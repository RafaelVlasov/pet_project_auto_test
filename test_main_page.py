from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object главной страницы, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_be_login_link()     # проверка наличия кнопки авторизации
    page.go_to_login_page()         # метод перехода на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object страницы авторизации
    login_page.should_be_login_page() # выполняем проверки на корректный url, наличие форм регистрации и авторизации
