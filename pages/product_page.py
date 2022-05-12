from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

# создаём класс страницы товара и наследуем его от класса BasePage определённом в файле base_page.py
class ProductPage(BasePage):
    def save_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
        
    def save_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
        
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
    
    def should_be_equal_price_and_name_product(self, product_name, product_price):
        """функция сравнения имени товара и его цены до добавления в корзину с именем и ценой после попадания в карзину"""
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert "added to your basket" in success_message, "Success message not found"
        assert product_name_in_basket == product_name, "Product name is not equal"
        assert product_price_in_basket == product_price, "Product name is not equal"

    def should_be_product_page(self, link):
        self.should_be_product_url(link)
        self.should_be_button_add_to_basket()

    def should_be_product_url(self, link):
        # проверка на корректный url адрес
        assert link[-32:] == self.browser.current_url[-32:], "Incorrect url"

    def should_be_button_add_to_basket(self):
        # проверка наличия кнопки добавления товара в корзину
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add product to basket not presented"

        # вычисление математической формулы и получение ответного значения
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
         
        # проверка, на отсутствие сообщения о добавлении товара в карзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
        # проверка на пропадание сообщения о добавлении товара в карзину
    def is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
