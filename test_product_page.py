import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) # инициализируем Page Object страницы товара, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                       # открываем страницу
    product_name = page.save_product_name()  # сохраняем значение имени товара
    product_price = page.save_product_price() # сохраняем значение стоимости товара
    page.should_be_product_page(link)     # проверка корректного url и наличия кнопки добавления товара в корзину
    page.add_product_to_basket()      # добавляем товар в карзину
    page.solve_quiz_and_get_code()    # вычисляем значение математической функции появившееся в alert и показываем его в консоли
    basket_page = ProductPage(browser, browser.current_url)
    basket_page.should_be_equal_price_and_name_product(product_name, product_price) # проверка совпадения цены и имени товара со страницы товара и страницы корзины
    
    








