import uuid
from selenium import webdriver
import unittest

from keywords.wait_until_is_visible import wait_until_home_page_is_visible, \
    wait_until_create_a_new_user_dialog_is_visible, wait_until_edie_user_page_is_visible
from test_post.TestPostCreate import sign_in_as_admin, sign_out, go_back_to_home_page_from_sign_in_page, \
    click_create_submit_button


def click_create_user_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


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
        self.driver.find_element_by_xpath('//*[@href="/keystone/users"]').click()
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abcc@ntut.org.tw'
        user_password = 'asdfasdfabaswef'
        user_password_confirm = 'asdfasdfabaswef'
        self.driver.find_element_by_xpath('//*[@name="name.first"]').send_keys(user_first_name)
        self.driver.find_element_by_xpath('//*[@name="name.last"]').send_keys(user_last_name)
        self.driver.find_element_by_xpath('//*[@name="email"]').send_keys(user_email)
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(user_password)
        self.driver.find_element_by_xpath('//*[@name="password_confirm"]').send_keys(user_password_confirm)
        click_create_submit_button(self)
        wait_until_edie_user_page_is_visible(self)
        self.driver.back()
        self.assertTrue(self.driver.find_element_by_link_text(user_first_name + ' ' + user_last_name) is not None)

    def test_create_user_with_wrong_email1(self):
        self.driver.find_element_by_xpath('//*[@href="/keystone/users"]').click()
        click_create_user_button(self)
        wait_until_create_a_new_user_dialog_is_visible(self)
        user_first_name = 'cheng an'
        user_last_name = 'chu'
        uuid1 = uuid.uuid1()
        user_email = str(uuid1) + 'abccntut.org.tw'
        user_password = 'asdfasdfabaswef'
        user_password_confirm = 'asdfasdfabaswef'
        self.driver.find_element_by_xpath('//*[@name="name.first"]').send_keys(user_first_name)
        self.driver.find_element_by_xpath('//*[@name="name.last"]').send_keys(user_last_name)
        self.driver.find_element_by_xpath('//*[@name="email"]').send_keys(user_email)
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(user_password)
        self.driver.find_element_by_xpath('//*[@name="password_confirm"]').send_keys(user_password_confirm)
        click_create_submit_button(self)

        # wait_until_edie_user_page_is_visible(self)

    def tearDown(self) -> None:
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
# todo: add all test print
