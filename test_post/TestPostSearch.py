import time

from selenium import webdriver
import unittest

from keywords.wait_until_is_visible import wait_until_home_page_is_visible
from test_post.TestPostCreate import sign_in_as_admin, create_a_post, delete_a_post, sign_out, \
    go_back_to_home_page_from_sign_in_page, go_to_posts_page_from_admin_ui_page


# todo: need refactor
class TestPostSearch(unittest.TestCase):
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

    def test_search_post_with_ISP_input1(self):
        post_name1 = 'post_name'  # todo: setup 錯地方?
        create_a_post(self, post_name1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_tag_name('input').send_keys(post_name1)
        self.assertTrue(len(self.driver.find_elements_by_link_text(post_name1)) > 0)
        print('test_search_post_with_ISP_input1 ok')
        delete_a_post(self, post_name1)

    def test_search_post_with_ISP_input2(self):
        post_name2 = 'post_name_post_namepost_namepost_namepost_namepost_namepost_namepost_namepost_namepost_namepost_name'
        create_a_post(self, post_name2)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_tag_name('input').send_keys(post_name2)
        self.assertTrue(len(self.driver.find_elements_by_link_text(post_name2)) > 0)
        print('test_search_post_with_ISP_input2 ok')
        delete_a_post(self, post_name2)

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
