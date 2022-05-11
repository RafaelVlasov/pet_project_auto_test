from selenium.webdriver.common.by import By
# классы для хранения переменных страниц объектов в которые сохраняем сущности передавая аргументами что мы ищим и каким способом

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")

