import time

from selenium import webdriver
import unittest

from keywords.on_admin_ui_page import click_a_dashboard_button
from keywords.wait_until_is_visible import wait_until_home_page_is_visible, wait_until_posts_page_is_visible, \
    wait_until_create_a_new_category_dialog_is_visible, wait_until_edit_category_page_is_visible
from test_post.TestPostCreate import sign_in_as_admin, click_create_submit_button, sign_out, \
    go_back_to_home_page_from_sign_in_page, scroll_page, click_go_back_to_posts_page_button


# on posts page
def click_create_category_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


def input_category_name(self, category_name):
    self.driver.find_element_by_name('name').send_keys(category_name)


# on posts page
def verify_categories_page_have_category(self, category_name):
    assert category_name in self.driver.find_element_by_xpath(
        '//*[contains(text(), ' + "\"" + category_name + "\"" + ')]').text


#######################################################################################################3
# on posts_page -> admin_ui_page
def go_to_categories_page_from_admin_ui_page(self):
    click_a_dashboard_button(self, 'Posts', 'Categories')
    wait_until_posts_page_is_visible(self)


# on posts_page -> create_a_new_post_dialog -> edit_post_page
def create_a_category(self, category_name):
    click_create_category_button(self)
    wait_until_create_a_new_category_dialog_is_visible(self)
    input_category_name(self, category_name)
    click_create_submit_button(self)
    wait_until_edit_category_page_is_visible(self)


# edit_page -> posts_page
def go_back_to_categories_page_from_edit_category(self):
    scroll_page(self, 0)
    time.sleep(5)
    click_go_back_to_posts_page_button(self)
    wait_until_posts_page_is_visible(self)


class TestCategoryCreate(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_create_a_category(self):
        go_to_categories_page_from_admin_ui_page(self)
        category_name = "category_name"
        create_a_category(self, category_name)
        self.driver.back()
        time.sleep(1)
        verify_categories_page_have_category(self, category_name)
        print("test_create_a_category ok")
        # todo: tearDown

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
