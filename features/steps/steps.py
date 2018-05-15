from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


@Given('Заходим на сайт "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@step('Вводим в поле для ввода информации "{word}"')
def step_impl(context, word):
    context.browser.find_element_by_xpath('//input[@id=\'search\']').send_keys(word)


@step('Нажимаем кнопку поиска')
def step_impl(context):
    context.browser.find_element_by_xpath('//button[@id="search-icon-legacy"]').click()
