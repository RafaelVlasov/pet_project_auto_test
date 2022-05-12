import pytest
from .pages.product_page import ProductPage


def test_guest_cant_see_success_message(browser):
    link  = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link) # инициализируем Page Object страницы товара, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                       # открываем страницу
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_not_be_success_message()
