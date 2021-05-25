from selenium import webdriver
import unittest

from selenium.common.exceptions import NoSuchElementException

from keywords.wait_until_is_visible import wait_until_home_page_is_visible
from test_post.TestPostCreate import sign_in_as_admin, go_to_posts_page_from_admin_ui_page, create_a_post, \
    delete_a_post, sign_out, go_back_to_home_page_from_sign_in_page


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
        post_name = 'abc'
        create_a_post(self, post_name)

    def test_delete_a_post(self):
        post_name = 'abc'
        self.driver.back()  # todo: 要移除?
        delete_a_post(self, post_name)
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text('This Post was created by selenium #Edit')
        print('test_delete_a_post ok')
        # todo: add print(message)!!!

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
