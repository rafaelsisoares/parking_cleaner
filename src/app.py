from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.consts import DISABLE_FEATURE
from cleaner import Cleaner


if __name__ == "__main__":
    # Adiciona opções para a instancia do navegador aberta pelo script
    options = Options()
    options.add_argument("--incognito")
    options.add_argument(f"--disable-features={DISABLE_FEATURE}")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Inicia a instancia do navegador controlada pelo codigo
    # O navegador usado pelo script (Chrome)
    browser = webdriver.Chrome(options=options)
    cleaner = Cleaner(browser)
    cleaner.start()
