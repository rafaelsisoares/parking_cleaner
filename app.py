from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from time import sleep
import os


def open_session() -> None:
    load_dotenv()
    url = os.getenv("URL")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=10)

    browser.get(url)
    input_email = wait.until(EC.visibility_of_element_located((By.ID, "inputEmail3")))
    input_password = wait.until(EC.visibility_of_element_located((By.ID, "inputPassword3")))
    btn_access = browser.find_element(by=By.LINK_TEXT, value="Acessar")
    input_email.send_keys(email)
    input_password.send_keys(password)
    btn_access.click()
    wait.until(EC.invisibility_of_element_located(btn_access))
    sleep(1)
    aside_menu = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "aside")))
    operations_menu = aside_menu.find_element(by=By.LINK_TEXT, value="Operações")
    operations_menu.click()
    operations_option = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Manutenção de Credenciais")))
    operations_option.click()
    search = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-success")))
    search.click()
    sleep(10)


if __name__ == "__main__":
    open_session()
