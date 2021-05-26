import time

from selenium import webdriver
import unittest

from selenium.common.exceptions import NoSuchElementException

from keywords.wait_until_is_visible import wait_until_home_page_is_visible, wait_until_comments_page_is_visible, \
    wait_until_delete_warning_dialog, wait_until_posts_page_is_visible, wait_until_edit_comment_page_is_visible
from test_comment.TestCommentCreate import go_to_admin_ui_page_from_comments_page, \
    go_to_comments_page_from_admin_ui_page, create_a_comment
from test_post.TestPostCreate import sign_in_as_admin, sign_out, go_back_to_home_page_from_sign_in_page, \
    go_to_posts_page_from_admin_ui_page, create_a_post


#############################################################################
def delete_a_comment(self, comment_id):
    self.driver.find_element_by_xpath('//*[@href="/keystone/post-comments/' + comment_id + '"]').click()
    wait_until_edit_comment_page_is_visible(self)
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()
    wait_until_delete_warning_dialog(self)
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()
    wait_until_comments_page_is_visible(self)


class TestPostCreate(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_delete_comment(self):
        # setup
        go_to_posts_page_from_admin_ui_page(self)
        post_name = 'post_name'
        create_a_post(self, post_name)
        go_to_admin_ui_page_from_comments_page(self)
        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        create_a_comment(self, comment_author, post_name)
        self.driver.back()  # todo: back?

        # delete comment
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        delete_a_comment(self, comment_id)
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text(comment_id)
        print('test_delete_comment ok')

    def tearDown(self) -> None:
        # todo: delete all post?
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
