from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NoteSeleniumTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_notes_can_be_created(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element(By.NAME, "title").send_keys("Selenium Note")
        self.browser.find_element(By.NAME, "description").send_keys("Valid description here")
        self.browser.find_element(By.NAME, "description").send_keys(Keys.RETURN)

        time.sleep(2)
        self.assertIn("Selenium Note", self.browser.page_source)

    def test_error_occurs_if_description_is_less_than_10_chars_long(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element(By.NAME, "title").send_keys("Bad Note")
        self.browser.find_element(By.NAME, "description").send_keys("short")
        self.browser.find_element(By.NAME, "description").send_keys(Keys.RETURN)

        time.sleep(2)
        self.assertIn("Description must be at least 10 characters long", self.browser.page_source)