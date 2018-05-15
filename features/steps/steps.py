from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


@Given('Заходим на сайт "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@Then('Находим поле для ввода информации')
def step_impl(context):
    search_field = context.browser.find_element_by_xpath('//input[@id=\'search\']')
    if search_field:
        context.search_field = search_field


@step('Вводим в поле для ввода информации "{word}"')
def step_impl(context, word):
    context.search_field.send_keys(word, Keys.ENTER)
