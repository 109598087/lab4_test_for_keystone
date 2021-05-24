import time

from selenium import webdriver
import unittest

from selenium.common.exceptions import NoSuchElementException

from keywords.on_sign_in_page import input_email, input_password, submit_email_and_password, click_logo_button
from keywords.wait_until_is_visible import wait_until_home_page_is_visible, wait_until_admin_ui_page_is_visible, \
    wait_until_posts_page_is_visible, wait_until_edit_post_page_is_visible, \
    wait_until_create_a_new_post_dialog_is_visible, wait_until_sign_in_page_is_visible, \
    wait_until_delete_warning_dialog, wait_until_delete_button_on_edit_post_page_is_visible, \
    wait_until_name_is_required_is_visible
from keywords.on_admin_ui_page import click_a_dashboard_button


# todo: variables post_name
# xpath example:  //*[contains(@id, "listHeaderSortButton")]

def click_sign_in_button(self):
    self.driver.find_element_by_xpath(
        '//*[contains(text(), "Sign in") and @href="/keystone/signin"]').click()


# on posts page
def click_create_post_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


# on posts page create a new post create_a_new_post_dialog
def input_post_name(self, post_name):
    self.driver.find_element_by_name('name').send_keys(post_name)


# on posts page create a new post create_a_new_post_dialog
def click_create_submit_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create") and @type="submit"]').submit()


# on posts page create a new post create_a_new_post_dialog -> posts page
def click_cancel_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Cancel") and @data-button-type="cancel"]').click()


# on edit_post_page
def click_go_back_to_posts_page_button(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/posts")]').click()


def click_a_post(self, post_name):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "ItemList") and contains(text(), ' + "\"" + post_name + "\"" + ')]').click()


# on posts page -> edit_post_page
def read_a_post(self, post_name):
    click_a_post(self, post_name)
    wait_until_edit_post_page_is_visible(self)


# on edit_post_page
def scroll_page(self, top):
    js = "document.documentElement.scrollTop=" + str(top)
    self.driver.execute_script(js)


# on edit post page
def click_delete_post_button(self):
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()


# on delete_warning_dialog
def click_delete_button(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()


# on posts page
def click_sign_out_button(self):
    self.driver.find_element_by_xpath('//*[@href = "/keystone/signout"]').click()


##########################################################################################
# on home page ->　sign_in_page -> admin_ui_page
def sign_in_as_admin(self):
    click_sign_in_button(self)
    wait_until_sign_in_page_is_visible(self)
    input_email(self)
    input_password(self)
    submit_email_and_password(self)
    wait_until_admin_ui_page_is_visible(self)


# on posts_page -> admin_ui_page
def go_to_posts_page_from_admin_ui_page(self):
    click_a_dashboard_button(self, 'Posts', 'Posts')
    wait_until_posts_page_is_visible(self)


# on posts_page -> create_a_new_post_dialog -> edit_post_page
def create_a_post(self, post_name):
    click_create_post_button(self)
    wait_until_create_a_new_post_dialog_is_visible(self)
    input_post_name(self, post_name)
    click_create_submit_button(self)
    wait_until_edit_post_page_is_visible(self)


# edit_page -> posts_page
def go_back_to_posts_page_from_edit_page(self):
    scroll_page(self, 0)
    time.sleep(5)
    click_go_back_to_posts_page_button(self)
    wait_until_posts_page_is_visible(self)


# on posts page
def verify_posts_page_have_post(self, post_name):
    assert post_name in self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]').text


# on posts page -> edit_post_page -> delete_warning_dialog -> posts_page
def delete_a_post(self, post_name):  # todo: 直接在posts page上delete post
    read_a_post(self, post_name)
    scroll_page(self, 10000)
    wait_until_delete_button_on_edit_post_page_is_visible(self)
    click_delete_post_button(self)
    wait_until_delete_warning_dialog(self)
    click_delete_button(self)
    wait_until_posts_page_is_visible(self)


# posts page -> sign in page
def sign_out(self):
    click_sign_out_button(self)
    wait_until_sign_in_page_is_visible(self)


# sign_in_page -> home_page
def go_back_to_home_page_from_sign_in_page(self):
    click_logo_button(self)


# def verify_posts_page_do_not_have_post(self):
#     with self.assertRaises(NoSuchElementException):
#         driver.find_element_by_link_text('This Post was created by selenium #Edit')


class TestPostCreate(unittest.TestCase):
    driver = None
    post_name1 = ""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_create_post_with_empty_post_name_and_fail(self):
        post_name = ''
        go_to_posts_page_from_admin_ui_page(self)
        click_create_post_button(self)
        wait_until_create_a_new_post_dialog_is_visible(self)
        input_post_name(self, post_name)
        click_create_submit_button(self)
        wait_until_name_is_required_is_visible(self)
        assert 'Name is required' in self.driver.find_element_by_xpath('//*[contains(@data-alert-type, "danger")]').text
        ##############
        # teardown
        click_cancel_button(self)

    def test_create_post_with_more_than_0_and_less_than_or_equal_to_50_post_name_length_successfully(self):
        past_name = 'abc'
        go_to_posts_page_from_admin_ui_page(self)
        create_a_post(self, past_name)
        go_back_to_posts_page_from_edit_page(self)
        verify_posts_page_have_post(self, past_name)
        ##############
        # teardown
        delete_a_post(self, past_name)

    def test_create_post_with_more_than_50_post_name_length_successfully(self):
        past_name = '01234567890123456789012345678901234567890123456789abcbasdfasdfasdf'
        go_to_posts_page_from_admin_ui_page(self)
        create_a_post(self, past_name)
        go_back_to_posts_page_from_edit_page(self)
        verify_posts_page_have_post(self, past_name)
        ##############
        # teardown
        delete_a_post(self, past_name)

    def test_create_post_click_cancel_button_and_post_should_not_be_create(self):
        post_name = 'abc'
        go_to_posts_page_from_admin_ui_page(self)
        click_create_post_button(self)
        wait_until_create_a_new_post_dialog_is_visible(self)
        input_post_name(self, post_name)
        click_cancel_button(self)
        try:
            self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]')
        except NoSuchElementException:
            assert NoSuchElementException

    def tearDown(self) -> None:
        # todo: delete all post?
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
