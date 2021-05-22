from selenium import webdriver
import unittest
# for wait until
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def sign_in_as_admin(self):
    self.driver.find_element_by_xpath(
        '//*[contains(text(), "Sign in") and @href="/keystone/signin"]').click()
    wait_until_sign_in_dialog_is_visible(self)
    self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')
    self.driver.find_element_by_name('password').send_keys('demo')
    self.driver.find_element_by_xpath('//*[contains(@type, "submit") and contains(text(), "Sign In")]').submit()


def sign_out(self):
    self.driver.find_element_by_xpath('//*[contains(@title, "Sign Out")]').click()


# click_a_dashboard.png
def click_a_dashboard(self, heading, label):  # todo: label 傳"Posts" (現在是傳"posts")
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "dashboard-group")]//*[contains(@data-section-label,' + heading + ')]//*[contains(@data-list-path, ' + label + ')]//*[contains(@class, "dashboard-group__list-tile")]').click()


def click_create_post_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


def input_post_name(self, post_name):
    self.driver.find_element_by_name('name').send_keys(post_name)


def click_create_submit_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create") and @type="submit"]').submit()


def go_back_keystone_posts_page_from_edit_post_page(self):  # todo: to -> back? ->button
    self.driver.find_element_by_xpath(
        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/posts")]').click()


def go_to_home_page_from_sign_in_page(self):
    self.driver.find_element_by_xpath('//*[contains(@class, "logo")]').click()


def verify_posts_page_have_post(self, post_name):
    assert post_name in self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]').text


def wait_until_edit_post_page_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/posts")]')


def wait_until_admin_ui_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "dashboard-group")]')


def wait_until_create_a_new_post_dialog_is_visible(self):
    wait_until_element_visible_by_name(self, 'name')


def wait_until_sign_in_dialog_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "logo")]')


def wait_until_posts_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Create ")]')


def wait_until_home_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Sign in") and @href="/keystone/signin"]')


def read_a_post(self, post_name):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "ItemList") and contains(text(), ' + "\"" + post_name + "\"" + ')]').click()
    wait_until_edit_post_page_is_visible(self)


def delete_a_post(self, post_name):
    read_a_post(self, post_name)
    js = "var q=document.documentElement.scrollTop=10000"
    self.driver.execute_script(js)
    wait_until_element_visible_by_xpath(self, '//*[contains(@data-button, "delete")]')
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]')
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()


def wait_until_element_visible_by_xpath(self, xpath):
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


def wait_until_element_visible_by_name(self, name):
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, name)))


# todo: variables post_name
# xpath example:  //*[contains(@id, "listHeaderSortButton")]
class TestPostFeatures(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_create_post_on_the_admin_ui_page_successfully(self):
        wait_until_admin_ui_page_is_visible(self)
        click_a_dashboard(self, 'Posts', 'posts')

        wait_until_posts_page_is_visible(self)
        click_create_post_button(self)

        wait_until_create_a_new_post_dialog_is_visible(self)
        input_post_name(self, 'abc')
        click_create_submit_button(self)

        wait_until_edit_post_page_is_visible(self)
        go_back_keystone_posts_page_from_edit_post_page(self)

        wait_until_posts_page_is_visible(self)
        verify_posts_page_have_post(self, 'abc')

    def tearDown(self) -> None:
        delete_a_post(self, 'abc')
        wait_until_posts_page_is_visible(self)
        sign_out(self)
        wait_until_sign_in_dialog_is_visible(self)
        go_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
