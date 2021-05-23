from selenium import webdriver
import unittest

from TestPostCreate import sign_in_as_admin, go_to_posts_page_from_admin_ui_page, create_a_post, delete_a_post, \
    go_back_to_posts_page_from_edit_page
from keywords.wait_until_is_visible import wait_until_home_page_is_visible


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
        pass

    def tearDown(self) -> None:
        post_name = 'abc'
        go_back_to_posts_page_from_edit_page(self)  # todo: 要移除?
        delete_a_post(self, post_name)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
