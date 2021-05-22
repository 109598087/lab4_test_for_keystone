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
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[contains(@type, "submit") and contains(text(), "Sign In")]')))  # sign in button visibility
    self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')
    self.driver.find_element_by_name('password').send_keys('demo')
    self.driver.find_element_by_xpath('//*[contains(@type, "submit") and contains(text(), "Sign In")]').submit()


def sign_out(self):
    self.driver.find_element_by_xpath('//*[contains(@title, "Sign Out")]').click()


# click_a_dashboard.png
def click_a_dashboard(self, heading, label):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "dashboard-group")]//*[contains(@data-section-label,' + heading + ')]//*[contains(@data-list-path, ' + label + ')]//*[contains(@class, "dashboard-group__list-tile")]').click()


def click_create_post_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


def input_post_name(self, post_name):
    self.driver.find_element_by_name('name').send_keys(post_name)


def click_create_submit_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create") and @type="submit"]').submit()


def go_to_keystone_posts_page_from_edit_post_page(self):  # todo: to -> back? ->button
    self.driver.find_element_by_xpath(
        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@data-e2e-editform-header-back, "true")]').click()


def go_to_keystone_home_page_from_sign_in_page(self):
    self.driver.find_element_by_xpath('//*[contains(@class, "logo")]').click()


def verify_keystone_posts_page_have_post(self, post_name):
    assert post_name in self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]').text


def delete_a_post(self, post_name):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "ItemList") and contains(text(), ' + "\"" + post_name + "\"" + ')]').click()
    wait_until_element_visible_by_xpath(self.driver,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@data-e2e-editform-header-back, "true")]')
    js = "var q=document.documentElement.scrollTop=10000"
    self.driver.execute_script(js)
    wait_until_element_visible_by_xpath(self.driver, '//*[contains(@data-button, "delete")]')
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()
    wait_until_element_visible_by_xpath(self.driver,
                                        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]')
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()


def wait_until_element_visible_by_xpath(driver, xpath):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, xpath)))  # sign in button visibility


def wait_until_element_visible_by_name(driver, name):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.NAME, name)))  # sign in button visibility


# todo: variables post_name
# xpath example:  //*[contains(@id, "listHeaderSortButton")]
class TestPostFeatures(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_element_visible_by_xpath(self.driver,
                                            '//*[contains(text(), "Sign in") and @href="/keystone/signin"]')
        sign_in_as_admin(self)

    def test_create_post_on_the_admin_ui_page_successfully(self):
        wait_until_element_visible_by_xpath(self.driver, '//*[contains(@class, "dashboard-group")]')
        click_a_dashboard(self, 'Posts', 'posts')

        wait_until_element_visible_by_xpath(self.driver, '//*[contains(text(), "Create ")]')

        click_create_post_button(self)

        wait_until_element_visible_by_name(self.driver, 'name')
        input_post_name(self, 'abc')
        click_create_submit_button(self)

        wait_until_element_visible_by_xpath(self.driver,
                                            '//*[contains(@data-e2e-editform-header-back, "true") and contains(@data-e2e-editform-header-back, "true")]')
        go_to_keystone_posts_page_from_edit_post_page(self)
        wait_until_element_visible_by_xpath(self.driver, '//*[contains(text(), ' + "abc" ')]')
        verify_keystone_posts_page_have_post(self, 'abc')

    def tearDown(self) -> None:
        delete_a_post(self, 'abc')
        wait_until_element_visible_by_xpath(self.driver, '//*[contains(text(), "Create ")]')
        sign_out(self)
        wait_until_element_visible_by_xpath(self.driver, '//*[contains(@class, "logo")]')
        go_to_keystone_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
