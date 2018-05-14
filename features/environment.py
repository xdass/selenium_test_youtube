from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    options = Options()
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(chrome_options=options)


def after_all(context):
    context.browser.quit()
