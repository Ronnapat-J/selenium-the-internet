from pages.login_page import LoginPage
import time

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.success_message_is_displayed()
    time.sleep(2)

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid", "wrongpass")
    assert login_page.error_message_is_displayed()
    time.sleep(2)

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.success_message_is_displayed()

    login_page.logout()
    # ตรวจสอบ URL หลังจาก logout
    assert "login" in driver.current_url  # URL ควรจะเป็น /login หรือมีคำว่า 'login' ใน URL
    time.sleep(2)