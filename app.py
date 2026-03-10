from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from time import sleep
from utils.consts import DISABLE_FEATURE, ID_EMAIL, ID_PASSWORD
import os


class Cleaner:
    def __init__(self, browser) -> None:
        load_dotenv()
        self.__browser = browser
        self.__wait = WebDriverWait(self.__browser, timeout=20)
        self.__url = os.getenv("URL")
        self.__email = os.getenv("EMAIL")
        self.__password = os.getenv("PASSWORD")
        self.__cleared_credentials = ""

    def __go_to_table(self) -> None:
        aside_menu = self.__wait.until(EC.visibility_of_element_located(
            (By.TAG_NAME, "aside")
        ))
        aside_menu.find_element(
            by=By.LINK_TEXT, value="Operações"
        ).click()
        self.__wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, "Manutenção de Credenciais")
        )).click()

    def __select_all(self) -> None:
        self.__wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "btn-success")
        )).click()
        pages = self.__wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "select-page"))).get_attribute("max")
        for _ in range(int(pages)):
            head = self.__wait.until(EC.visibility_of_element_located(
                (By.TAG_NAME, "thead")
            ))
            label = head.find_element(by=By.TAG_NAME, value="label")
            label.find_element(by=By.TAG_NAME, value="span").click()
            self.__browser.find_element(by=By.LINK_TEXT, value=">").click()
        footer = self.__browser.find_elements(
            by=By.CLASS_NAME, value="col-lg-12"
        )[-1]
        btn_clear = footer.find_element(by=By.TAG_NAME, value="button")
        self.__cleared_credentials = btn_clear.find_element(
            by=By.TAG_NAME, value="span"
        ).get_attribute("textContent")
        btn_clear.click()

    def __finish_clear(self) -> None:
        panel = self.__wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "panel-body")
        ))
        select = panel.find_element(by=By.ID, value="ReasonMaintenance")
        reasons = Select(select)
        reasons.select_by_visible_text("LIMPEZA DE PÁTIO")
        panel_footer = self.__browser.find_element(
            by=By.CLASS_NAME, value="panel-footer"
        )
        panel_footer.find_element(
            by=By.CLASS_NAME, value="btn-primary"
        ).click()
        self.__wait.until(EC.invisibility_of_element_located(panel))

    def start(self) -> None:
        self.__browser.get(self.__url)
        self.__wait.until(EC.visibility_of_element_located(
            (By.ID, ID_EMAIL))).send_keys(self.__email)
        self.__wait.until(EC.visibility_of_element_located(
            (By.ID, ID_PASSWORD))).send_keys(self.__password)
        self.__browser.find_element(by=By.LINK_TEXT, value="Acessar").click()
        self.__wait.until(EC.invisibility_of_element_located(
            (By.LINK_TEXT, "Acessar")
        ))
        sleep(1)
        self.__go_to_table()
        self.__select_all()
        self.__finish_clear()
        print(
            f"##############################################################\n"
            f"O pátio foi limpo, {self.__cleared_credentials} credenciais fechadas.\n"
            f"##############################################################\n"
        )
        self.__browser.quit()


def open_session() -> None:
    load_dotenv()
    url = os.getenv("URL")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    cleared_credentials = ""

    options = Options()
    options.add_argument(f"--disable-features={DISABLE_FEATURE}")
    options.add_argument("--disable-web-security")
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options)
    wait = WebDriverWait(browser, timeout=20)

    browser.get(url)
    input_email = wait.until(EC.visibility_of_element_located(
        (By.ID, ID_EMAIL)))
    input_password = wait.until(EC.visibility_of_element_located(
        (By.ID, ID_PASSWORD)))
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
    panel = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "panel-body")))
    select = panel.find_element(by=By.ID, value="ReasonMaintenance")
    reasons = Select(select)
    reasons.select_by_visible_text("LIMPEZA DE PÁTIO")
    panel_footer = browser.find_element(by=By.CLASS_NAME, value="panel-footer")
    btn_save = panel_footer.find_element(by=By.CLASS_NAME, value="btn-primary")
    btn_save.click()
    wait.until(EC.invisibility_of_element_located(panel))
    os.system("clear")
    print(
        f"##############################################################\n"
        f"O pátio foi limpo, {cleared_credentials} credenciais fechadas.\n"
        f"##############################################################\n"
        )
    browser.quit()


if __name__ == "__main__":
    options = Options()
    options.add_argument(f"--disable-features={DISABLE_FEATURE}")
    options.add_argument("--disable-web-security")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=options)
    cleaner = Cleaner(browser)
    cleaner.start()
