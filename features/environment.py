from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    # chrome_path = getcwd() + '/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(chrome_options=options)


def after_all(context):
    context.browser.close()
    context.browser.quit()
