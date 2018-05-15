from behave import *


@Given('Заходим на сайт "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@Then('Находим поле для ввода информации')
def step_impl(context):
    context.browser.find_element_by_xpath('//input[@id=\'search\']')
