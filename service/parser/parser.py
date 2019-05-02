from selenium import webdriver
from config.constant.module import PARSER
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.constant.exit_code import PARSER
from config.constant.module import PARSER
import logging

LOGGER = logging.getLogger(PARSER)


class FriendsParser:
    def __enter__(self):
        try:
            self._driver = webdriver.Firefox()
            return self
        except Exception as ex:
            LOGGER.fatal(ex)
            exit(PARSER)

    def go(self, url):
        self._driver.get(url)

    def sing_in(self, log, passwd):
        login = self._driver.find_element_by_name("email")
        login.send_keys(log)
        password = self._driver.find_element_by_name("pass")
        password.send_keys(passwd, Keys.ENTER)

    def find_friends_page(self):
        self._driver.implicitly_wait(20)
        self._driver.find_element_by_tag_name("html").send_keys(Keys.LEFT_SHIFT + Keys.LEFT_ALT + '2')
        #profile = self._driver.find_element_by_xpath("//div[@id='pagelet_bluebar']//a[@accesskey='2']")
        #profile.send_keys(Keys.ENTER)
        self._driver.implicitly_wait(20)
        friends_link = self._driver.find_element_by_xpath("//div[@id='fbTimelineHeadline']//a[@data-tab-key='friends']")
        friends_link.send_keys(Keys.ENTER)

    def calculate_friends(self):
        self._driver.implicitly_wait(20)
        friends_a = self._driver.find_elements_by_css_selector("div.uiProfileBlockContent div a:first-child")
        LOGGER.info(f"Friends count: {len(friends_a)}")
        for friend in friends_a:
            LOGGER.info(f"{friend.text}: {friend.get_attribute('href')}")


    def _get_element(self, by, element, wait=20):
        try:
            result = WebDriverWait(self._driver, wait).until(
                EC.presence_of_element_located((by, element))
            )
            return result
        finally:
            self._driver.quit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.close()
