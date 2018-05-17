import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from utils import save_text_to_file


@Given('Заходим на сайт "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@step('Вводим в поле для ввода информации "{word}"')
def step_impl(context, word):
    element = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )
    element.send_keys("Jenkins")


@step('Нажимаем кнопку поиска')
def step_impl(context):
    # element = WebDriverWait(context.browser, 15).until(
    #     EC.visibility_of_element_located((By.XPATH, "//button[@id='search-icon-legacy'']"))
    # )
    #print(element)
    element = context.browser.find_element_by_xpath("//button[@id='search-icon-legacy']")
    element.click()


@Then('Переходим по ссылке на первое видео')
def step_impl(context):
    #element_xpath = "//div[@id='primary']//div[@id='contents' and contains(@class, 'ytd-item-section-renderer')]/*[1]"
    element = WebDriverWait(context.browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#contents a > h3:first-child"))
    )
    element.click()


@Then('Извлекаем описание видео')
def step_impl(context):
    element_xpath = "//div[@id='content']//yt-formatted-string[@id='description' and contains(@class, 'ytd-video-secondary-info-renderer')]"
    element = WebDriverWait(context.browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > #description"))
    )
    context.video_description = element.get_attribute("innerText")


@step('Сохраняем описание видео в файл')
def step_impl(context):
    save_text_to_file('video_description.txt', context.video_description)


@Then('Делаем скриншот старницы видео')
def step_impl(context):
    context.browser.save_screenshot('video_page.jpg')
