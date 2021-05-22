from selenium import webdriver
import unittest
import time


def sign_in_as_admin(self):
    self.driver.find_element_by_xpath(
        '//*[contains(text(), "Sign in") and @href="/keystone/signin"]').click()
    time.sleep(5)
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


def go_to_keystone_posts_page_from_edit_post_page(self):  # to -> back?
    self.driver.find_element_by_xpath(
        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@data-e2e-editform-header-back, "true")]').click()


def go_to_keystone_home_page_from_sign_in_page(self):
    self.driver.find_element_by_xpath('//*[contains(@class, "logo")]').click()


def verify_keystone_posts_page_have_post(self, post_name):
    assert post_name in self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]').text


def delete_a_post(self, post_name):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "ItemList") and contains(text(), ' + "\"" + post_name + "\"" + ')]').click()
    time.sleep(2)
    js = "var q=document.documentElement.scrollTop=10000"
    self.driver.execute_script(js)
    time.sleep(2)
    self.driver.find_element_by_xpath('//*[contains(@data-button, "delete")]').click()
    self.driver.find_element_by_xpath(
        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]').click()


# todo: varibles post_name
# xpath example:  //*[contains(@id, "listHeaderSortButton")]
class TestPostFeatures(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        time.sleep(1)  # todo: wait
        sign_in_as_admin(self)
        time.sleep(1)

    def test_create_post_on_the_admin_ui_page_successfully(self):
        time.sleep(2)
        click_a_dashboard(self, 'Posts', 'posts')
        time.sleep(2)
        click_create_post_button(self)
        time.sleep(1)
        input_post_name(self, 'abc')
        time.sleep(1)
        click_create_submit_button(self)
        time.sleep(1)
        go_to_keystone_posts_page_from_edit_post_page(self)
        time.sleep(1)
        verify_keystone_posts_page_have_post(self, 'abc')

    def tearDown(self) -> None:
        delete_a_post(self, 'abc')
        time.sleep(1)
        sign_out(self)
        time.sleep(1)
        go_to_keystone_home_page_from_sign_in_page(self)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
