from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    def success_message_is_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "flash"))
            )
            message = self.driver.find_element(By.ID, "flash").text
            return "You logged into a secure area!" in message
        except:
            return False
    def error_message_is_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "flash"))
            )
            error_message = self.driver.find_element(By.ID, "flash").text
            return "Your username is invalid!" in error_message
        except:
            return False
    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

