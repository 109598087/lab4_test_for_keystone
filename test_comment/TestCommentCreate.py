import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys

from keywords.on_admin_ui_page import click_a_dashboard_button
from keywords.wait_until_is_visible import wait_until_home_page_is_visible, wait_until_posts_page_is_visible, \
    wait_until_element_visible_by_xpath
from test_post.TestPostCreate import sign_in_as_admin, sign_out, go_back_to_home_page_from_sign_in_page, \
    click_create_submit_button


# on posts_page -> admin_ui_page
def go_to_posts_page_from_admin_ui_page(self):
    click_a_dashboard_button(self, 'Posts', 'Comments')
    wait_until_posts_page_is_visible(self)


def click_create_comment_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


def input_comment_author(self, comment_author):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[@class = "Select-arrow"]').click()
    time.sleep(2)  # todo: wait
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(comment_author)
    time.sleep(2)  # todo: wait
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(Keys.ENTER)


def input_comment_post(self, post_name):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="post"]//*[@class = "Select-arrow"]').click()
    time.sleep(2)  # todo: wait
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="post"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(post_name)
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="post"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(Keys.ENTER)


#########################################################################################
def wait_until_create_a_new_comment_dialog_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[@class="css-s2cbvv"]')


def create_a_comment(self, comment_author, post_name):
    click_create_comment_button(self)
    wait_until_create_a_new_comment_dialog_is_visible(self)
    input_comment_author(self, comment_author)
    input_comment_post(self, post_name)
    click_create_submit_button(self)


class TestCommentCreate(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_create_comment_with_ISP_input(self):
        go_to_posts_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'for_comment'
        create_a_comment(self, comment_author, post_name)

    def tearDown(self) -> None:
        # todo: delete all comment?
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
