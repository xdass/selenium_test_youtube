from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_path = getcwd() + '/chromedriver'
    options = Options()
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)


def after_all(context):
    context.browser.quit()
