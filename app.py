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
    cleared_credentials = 0

    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, timeout=10)

    browser.get(url)
    input_email = wait.until(EC.visibility_of_element_located(
        (By.ID, "inputEmail3")))
    input_password = wait.until(EC.visibility_of_element_located(
        (By.ID, "inputPassword3")))
    btn_access = browser.find_element(by=By.LINK_TEXT, value="Acessar")
    input_email.send_keys(email)
    input_password.send_keys(password)
    btn_access.click()
    wait.until(EC.invisibility_of_element_located(btn_access))
    sleep(1)
    aside_menu = wait.until(EC.visibility_of_element_located(
        (By.TAG_NAME, "aside")))
    operations_menu = aside_menu.find_element(
        by=By.LINK_TEXT, value="Operações"
        )
    operations_menu.click()
    operations_option = wait.until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Manutenção de Credenciais")))
    operations_option.click()
    search = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btn-success")))
    search.click()
    pages = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "select-page")))
    num_pages = int(pages.get_attribute("max"))
    for _ in range(num_pages):
        head = wait.until(EC.visibility_of_element_located(
            (By.TAG_NAME, "thead")))
        label = head.find_element(by=By.TAG_NAME, value="label")
        checkbox = label.find_element(by=By.TAG_NAME, value="span")
        checkbox.click()
        next_page = browser.find_element(by=By.LINK_TEXT, value=">")
        next_page.click()
    footer = browser.find_elements(by=By.CLASS_NAME, value="col-lg-12")[-1]
    btn_clear = footer.find_element(by=By.TAG_NAME, value="button")
    cleared_credentials = btn_clear.find_element(
        by=By.TAG_NAME, value="span"
        ).get_attribute("textContent")
    btn_clear.click()
    sleep(5)


if __name__ == "__main__":
    open_session()
