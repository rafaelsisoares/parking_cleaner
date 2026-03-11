from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
from time import sleep
from utils.consts import DISABLE_FEATURE, ID_EMAIL, ID_PASSWORD, OP, MC, LP
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
            by=By.LINK_TEXT, value=OP
        ).click()
        self.__wait.until(EC.visibility_of_element_located(
            (By.LINK_TEXT, MC)
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
        self.__wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "option"))
        )
        select = panel.find_element(by=By.ID, value="ReasonMaintenance")
        reasons = Select(select)
        reasons.select_by_visible_text(LP)
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
            f"O pátio foi limpo, "
            f"{self.__cleared_credentials} credenciais fechadas.\n"
            f"##############################################################\n"
        )
        self.__browser.quit()


if __name__ == "__main__":
    options = Options()
    options.add_argument(f"--disable-features={DISABLE_FEATURE}")
    options.add_argument("--disable-web-security")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=options)
    cleaner = Cleaner(browser)
    cleaner.start()
