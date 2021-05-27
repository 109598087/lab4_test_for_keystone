import time
import uuid
from selenium import webdriver
import unittest

from keywords.wait_until_is_visible import wait_until_home_page_is_visible, \
    wait_until_create_a_new_user_dialog_is_visible, wait_until_edit_user_page_is_visible, \
    wait_until_users_page_is_visible, wait_until_name_error_message_is_visible
from test_post.TestPostCreate import sign_in_as_admin, sign_out, go_back_to_home_page_from_sign_in_page, \
    click_create_submit_button


def click_create_user_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


def go_to_users_page_from_admin_ui_page(self):
    self.driver.find_element_by_xpath('//*[@href="/keystone/users"]').click()
    wait_until_users_page_is_visible(self)


def input_user_first_name(self, user_first_name):
    self.driver.find_element_by_xpath('//*[@name="name.first"]').send_keys(user_first_name)


def input_user_last_name(self, user_last_name):
    self.driver.find_element_by_xpath('//*[@name="name.last"]').send_keys(user_last_name)


def input_user_email(self, user_email):
    self.driver.find_element_by_xpath('//*[@name="email"]').send_keys(user_email)


def input_user_password(self, user_password):
    self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(user_password)


def input_user_password_confirm(self, user_password_confirm):
    self.driver.find_element_by_xpath('//*[@name="password_confirm"]').send_keys(user_password_confirm)


def go_to_users_page_from_edit_user_page(self):
    self.driver.find_element_by_xpath('//*[@href="/keystone/users" and @class="css-dmf4a8"]').click()
    wait_until_users_page_is_visible(self)


def click_close_button(self):
    self.driver.find_element_by_xpath('//*[@class="css-rd63ky"]').click()
    wait_until_users_page_is_visible(self)


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

    def test_create_user_successfully(self):
        go_to_users_page_from_admin_ui_page(self)

        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abcc@ntut.org.tw'
        user_password = 'asdfasdfabaswef'
        user_password_confirm = 'asdfasdfabaswef'
        input_user_first_name(self, user_first_name)
        input_user_last_name(self, user_last_name)
        input_user_email(self, user_email)
        input_user_password(self, user_password)
        input_user_password_confirm(self, user_password_confirm)
        click_create_submit_button(self)
        wait_until_edit_user_page_is_visible(self)
        self.driver.back()
        self.assertTrue(self.driver.find_element_by_link_text(user_first_name + ' ' + user_last_name) is not None)
        print('test_create_user_successfully ok')

    def test_create_user_with_same_email(self):
        go_to_users_page_from_admin_ui_page(self)
        # create user
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abcc@ntut.org.tw'
        user_password = 'asdfasdfabaswef'
        user_password_confirm = 'asdfasdfabaswef'
        input_user_first_name(self, user_first_name)
        input_user_last_name(self, user_last_name)
        input_user_email(self, user_email)
        input_user_password(self, user_password)
        input_user_password_confirm(self, user_password_confirm)
        click_create_submit_button(self)
        wait_until_edit_user_page_is_visible(self)
        go_to_users_page_from_edit_user_page(self)

        # create user with same email
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        user_password = 'asdfasdfabaswef'
        user_password_confirm = 'asdfasdfabaswef'
        input_user_first_name(self, user_first_name)
        input_user_last_name(self, user_last_name)
        input_user_email(self, user_email)
        input_user_password(self, user_password)
        input_user_password_confirm(self, user_password_confirm)
        click_create_submit_button(self)
        wait_until_name_error_message_is_visible(self)
        assert 'MongoError: E11000 duplicate key error collection: admin.users index: email_1 dup key: { email: ' + "\"" + user_email + "\"" + ' }' in self.driver.find_element_by_xpath(
            '//*[@data-alert-type="danger"]').text
        click_close_button(self)

        wait_until_users_page_is_visible(self)
        print('test_create_user_with_same_email ok')

    def test_create_user_with_common_password(self):
        go_to_users_page_from_admin_ui_page(self)
        # create user
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abcc@ntut.org.tw'
        user_password = 'password'
        user_password_confirm = 'password'
        input_user_first_name(self, user_first_name)
        input_user_last_name(self, user_last_name)
        input_user_email(self, user_email)
        input_user_password(self, user_password)
        input_user_password_confirm(self, user_password_confirm)
        click_create_submit_button(self)
        wait_until_name_error_message_is_visible(self)
        assert 'Password must not be a common, frequently-used password.' in self.driver.find_element_by_xpath(
            '//*[@data-alert-type="danger"]').text
        click_close_button(self)

    def test_create_user_with_wrong_password_confirm(self):
        go_to_users_page_from_admin_ui_page(self)
        # create user
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abcc@ntut.org.tw'
        user_password = 'asdfasdfsadfasdf'
        user_password_confirm = 'sadfsdfsdfsafasf'
        input_user_first_name(self, user_first_name)
        input_user_last_name(self, user_last_name)
        input_user_email(self, user_email)
        input_user_password(self, user_password)
        input_user_password_confirm(self, user_password_confirm)
        click_create_submit_button(self)
        wait_until_name_error_message_is_visible(self)
        assert 'Passwords must match.' in self.driver.find_element_by_xpath('//*[@data-alert-type="danger"]').text
        click_close_button(self)

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
# todo: add all test print
