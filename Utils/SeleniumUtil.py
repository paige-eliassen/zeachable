import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtils:
    def __init__(self):
        self.service = Service(executable_path='/Users/paigeliassen/PycharmProjects/zeachable/webdrivers/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = 20

    def go_to_url(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(locator)).click()

    def fill_form(self, locator, input_text):
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(locator)).send_keys(input_text)

    def get_page_title(self):
        return self.driver.title

    def close_browser(self):
        self.driver.close()

    def get_console_log(self):
        return self.driver.get_log

    def get_page_source(self):
        return self.driver.page_source

    def maximize_window(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()




