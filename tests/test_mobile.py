import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from configs import LOGIN, PASSWORD
from selenium.webdriver.common.action_chains import ActionChains


def _login_in_profile(browser):
    browser.find_element(By.XPATH, '/html/body/div[1]/header/div/a').click()
    time.sleep(2)
    browser.find_element(By.ID, ":r3:").send_keys(LOGIN)
    browser.find_element(By.ID, ":r4:").send_keys(PASSWORD)
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/form/button").click()


def _log_out(browser):
    browser.find_element(By.XPATH, '/html/body/div[1]/header/div/button').click()
    time.sleep(2)

    exit_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/ul/li')

    # Прокручиваем до элемента
    actions = ActionChains(browser)
    actions.move_to_element(exit_btn).perform()

    exit_btn.click()


def _reset_password(browser):
    browser.find_element(By.XPATH, '/html/body/div[1]/header/div/a').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/a').click()
    time.sleep(2)
    _reset_password_test_invalid_phone_numbers(browser)
    time.sleep(2)
    _reset_password_test_valid_phone_numbers(browser)


def _reset_password_test_invalid_phone_numbers(browser):
    print(f"\n_reset_password_test_invalid_phone_numbers - BEGIN")
    browser.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[2]/div/input').send_keys("")

    phone_input = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/div[2]/div/input")

    # Создайте список тестовых номеров телефонов для проверки валидации
    invalid_test_phone_numbers = ["123", "555-555-5555", "abc", "00"]

    # Переберите тестовые номера телефонов
    for phone_number in invalid_test_phone_numbers:
        # Очистите поле ввода
        # phone_input.clear()
        browser.execute_script("arguments[0].value = '';", phone_input)

        # Введите тестовый номер телефона
        phone_input.send_keys(phone_number)
        browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/button").click()

        # Найдите элементы с сообщениями об ошибках или индикаторами валидации на странице и проверьте их содержание
        error_messages = browser.find_elements(By.XPATH, "/html/body/div/div[2]/div[2]/form/div[2]/p")

        if error_messages:
            print(f"\nСообщение об ошибке: {error_messages[0].text}, Test case:  {phone_number}")
        else:
            print("Сообщение об ошибке не найдено.")
        time.sleep(2)
    print(f"\n_reset_password_test_valid_phone_numbers - END\n\n")


def _reset_password_test_valid_phone_numbers(browser):
    print(f"\n_reset_password_test_valid_phone_numbers - BEGIN")
    valid_test_phone_numbers = ["880342200", "123456789", "001880101"]  # 987105555

    # Переберите тестовые номера телефонов
    for phone_number in valid_test_phone_numbers:
        # Очистите поле ввода
        # phone_input.clear()
        browser.get("https://m.development55.tj/forgot-password")
        time.sleep(2)
        phone_input = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/div[2]/div/input")

        browser.execute_script("arguments[0].value = '';", phone_input)

        # Введите тестовый номер телефона
        phone_input.send_keys(phone_number)
        browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/form/button").click()
        print(f"\n Test case:  {phone_number}")
        time.sleep(3)

    print(f"\n_reset_password_test_valid_phone_numbers - END\n\n")


def test_mobile():
    browser = webdriver.Chrome()
    browser.get("https://m.development55.tj/")
    time.sleep(5)
    # 987105555

    _login_in_profile(browser)
    time.sleep(5)

    _log_out(browser)
    time.sleep(5)

    _reset_password(browser)

    time.sleep(2)
    browser.quit()
