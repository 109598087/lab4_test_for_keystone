import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys

from keywords.wait_until_is_visible import wait_until_home_page_is_visible, \
    wait_until_edit_comment_page_is_visible, wait_until_delete_warning_dialog, wait_until_comments_page_is_visible
from test_comment.TestCommentCreate import go_to_comments_page_from_admin_ui_page, create_a_comment, \
    input_comment_author, input_comment_post, go_to_admin_ui_page_from_comments_page, verify_comments_page_have_comment
from test_post.TestPostCreate import sign_in_as_admin, sign_out, go_back_to_home_page_from_sign_in_page, create_a_post, \
    go_to_posts_page_from_admin_ui_page


# from test_post.TestPostEdit import click_save_button
def delete_a_comment(self, comment_id):
    self.driver.find_element_by_xpath('//*[@href="/keystone/post-comments/' + comment_id + '"]').click()
    wait_until_edit_comment_page_is_visible(self)
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()
    wait_until_delete_warning_dialog(self)
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()
    wait_until_comments_page_is_visible(self)


def click_comment_state_select_arrow(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="commentState"]//*[@class = "Select-arrow"]').click()


def input_select_comment_state(self, comment_state):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="commentState"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(comment_state)


def click_save_button(self):
    self.driver.find_element_by_xpath('//*[@data-button = "update"]').click()


##############################################################
def input_comment_state(self, comment_state):
    click_comment_state_select_arrow(self)
    time.sleep(2)  # todo: wait
    input_select_comment_state(self, comment_state)
    time.sleep(2)  # todo: wait
    input_select_comment_state(self, Keys.ENTER)


def save_edit_comment(self):
    click_save_button(self)


def input_comment_content(self, comment_content):
    self.driver.switch_to.frame(0)
    self.driver.find_element_by_tag_name('body').send_keys(comment_content)
    self.driver.switch_to.default_content()


def verify_edit_comment_successfully(self):
    assert 'Your changes have been saved successfully' in self.driver.find_element_by_xpath(  # todo: 包起來
        '//*[@data-alert-type = "success"]').text


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

    def test_edit_comment_with_ISP_input1(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = ""
        comment_state = 'Pu'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        assert 'Your changes have been saved successfully' in self.driver.find_element_by_xpath(
            '//*[@class= "css-ctpeu"]').text
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')

    def test_edit_comment_with_ISP_input2(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = "comment_content"
        comment_state = 'Draft'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        time.sleep(2)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input3(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = "comment_content_comment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_content"
        comment_state = 'Archived'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input4(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = ""
        comment_state = 'Draft'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input5(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = "comment_content_comment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_content"
        comment_state = 'Published'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input6(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = "comment_content"
        comment_state = 'Archived'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input7(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        post_name = 'post_name'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = "comment_content_comment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_contentcomment_content"
        comment_state = 'Draft'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    def test_edit_comment_with_ISP_input8(self):
        # create post
        go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
        post_name = 'post_name'
        create_a_post(self, post_name)

        go_to_admin_ui_page_from_comments_page(self)

        go_to_comments_page_from_admin_ui_page(self)
        comment_author = 'Demo User'
        create_a_comment(self, comment_author, post_name)

        # Edit comment
        comment_content = ""
        comment_state = 'Archieved'
        input_comment_author(self, comment_author)
        input_comment_post(self, post_name)
        input_comment_state(self, comment_state)
        input_comment_content(self, comment_content)
        save_edit_comment(self)
        verify_edit_comment_successfully(self)
        self.driver.back()  # todo: back?
        comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
        verify_comments_page_have_comment(self, comment_id)
        print('test_edit_comment_with_ISP_input ok')
        delete_a_comment(self, comment_id)

    # def test_edit_comment_with_ISP_input9(self):
    #     # create post
    #     go_to_posts_page_from_admin_ui_page(self)  # todo: 整理page
    #     post_name = 'post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name_post_name'
    #     create_a_post(self, post_name)
    #
    #     go_to_admin_ui_page_from_comments_page(self)
    #
    #     go_to_comments_page_from_admin_ui_page(self)
    #     comment_author = 'Demo User'
    #     create_a_comment(self, comment_author, post_name)
    #
    #     # Edit comment
    #     comment_content = "comment_content"
    #     comment_state = 'Published'
    #     input_comment_author(self, comment_author)
    #     input_comment_post(self, post_name)
    #     input_comment_state(self, comment_state)
    #     input_comment_content(self, comment_content)
    #     save_edit_comment(self)
    #     verify_edit_comment_successfully(self)
    #     self.driver.back()  # todo: back?
    #     comment_id = self.driver.find_element_by_xpath('//*[contains(@href, "/keystone/post-comments/")]').text
    #     verify_comments_page_have_comment(self, comment_id)
    #     print('test_edit_comment_with_ISP_input ok')

    def tearDown(self) -> None:
        # todo: delete all post?
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
