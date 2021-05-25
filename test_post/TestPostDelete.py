import time

from selenium import webdriver
import unittest

from selenium.common.exceptions import NoSuchElementException

from keywords.wait_until_is_visible import wait_until_home_page_is_visible, \
    wait_until_delete_button_on_edit_post_page_is_visible, wait_until_delete_warning_dialog
from test_post.TestPostCreate import sign_in_as_admin, go_to_posts_page_from_admin_ui_page, create_a_post, \
    delete_a_post, sign_out, go_back_to_home_page_from_sign_in_page, read_a_post, scroll_page, click_delete_post_button, \
    click_cancel_button, verify_posts_page_have_post


class TestPostDelete(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)
        go_to_posts_page_from_admin_ui_page(self)

    def test_delete_a_post_with_ISP_input1(self):
        post_name1 = 'abc'
        create_a_post(self, post_name1)
        self.driver.back()  # todo: 要移除?
        delete_a_post(self, post_name1)
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text(post_name1)
        print('test_delete_a_post_with_ISP_input1 ok')
        # todo: add print(message)!!!

    def test_delete_a_post_with_ISP_input2(self):
        post_name2 = 'abcpost_name_post_name2_post_name2_post_name2post_name2post_name2post_name2post_namee2'
        create_a_post(self, post_name2)
        self.driver.back()  # todo: 要移除?
        delete_a_post(self, post_name2)
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text(post_name2)
        print('test_delete_a_post_with_ISP_input2 ok')
        # todo: add print(message)!!!

    def test_create_post_click_cancel_button_and_post_should_not_be_create(self):
        post_name1 = 'abc'
        create_a_post(self, post_name1)
        self.driver.back()  # todo: 要移除?
        read_a_post(self, post_name1)
        scroll_page(self, 10000)
        wait_until_delete_button_on_edit_post_page_is_visible(self)
        click_delete_post_button(self)
        wait_until_delete_warning_dialog(self)
        click_cancel_button(self)
        self.driver.back()
        verify_posts_page_have_post(self, post_name1)
        print('test_create_post_click_cancel_button_and_post_should_not_be_create ok')

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
