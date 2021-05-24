import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys

from TestPostCreate import sign_in_as_admin, go_to_posts_page_from_admin_ui_page, create_a_post, delete_a_post, \
    go_back_to_posts_page_from_edit_page
from keywords.wait_until_is_visible import wait_until_home_page_is_visible


def click_post_state_select_arrow(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[@class = "Select-arrow"]').click()


def input_select_post_state(self, post_state):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[contains(@aria-activedescendant, "react-select-2")]') \
        .send_keys(post_state)


##############################################################################################
def input_post_state(self, post_state):
    click_post_state_select_arrow(self)
    input_select_post_state(self, post_state)
    input_select_post_state(self, Keys.ENTER)


class TestPostEdit(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)
        go_to_posts_page_from_admin_ui_page(self)
        post_name = 'abc'
        create_a_post(self, post_name)

    def test_edit_post_with_ISP_input1(self):
        post_state1 = 'Draft'
        post_state2 = 'Published'
        post_state3 = 'Archived'

        post_author = 'Demo User'
        post_published_date = '20210520'  # todo: error日期
        post_content_brief = ''
        post_content_extended = ''
        input_post_state(self, post_state1)
        time.sleep(5)

    def tearDown(self) -> None:
        post_name = 'abc'
        go_back_to_posts_page_from_edit_page(self)  # todo: 要移除?
        delete_a_post(self, post_name)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
