import pytest
from .pages.product_page import ProductPage


def test_message_disappeared_after_adding_product_to_basket(browser):
    link  = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link) # инициализируем Page Object страницы товара, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                       # открываем страницу
    page.add_product_to_basket()      # добавляем товар в карзину
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.is_disappeared()
    
    

