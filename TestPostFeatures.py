from selenium import webdriver
import unittest
# for sign in
from on_sign_in_page import input_email, input_password, submit_email_and_password, click_logo_button
# for wait until
from wait_until_is_visible import wait_until_home_page_is_visible, wait_until_admin_ui_page_is_visible, \
    wait_until_posts_page_is_visible, wait_until_edit_post_page_is_visible, \
    wait_until_create_a_new_post_dialog_is_visible, wait_until_sign_in_page_is_visible, \
    wait_until_delete_warning_dialog, wait_until_delete_button_on_edit_post_page_is_visible


# on posts page
def click_sign_in_button(self):
    self.driver.find_element_by_xpath(
        '//*[contains(text(), "Sign in") and @href="/keystone/signin"]').click()


# on admin_ui_page
def click_a_dashboard_button(self, heading, label):  # todo: 拉出去
    self.driver.find_element_by_xpath(
        '//*[contains(@data-section-label,' + heading + ')]//*[contains(@class, "dashboard-group__list-label") and text()=' + "\"" + label + "\"" + ']').click()


# on posts page
def click_create_post_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create ")]').click()


# on posts page create a new post create_a_new_post_dialog
def input_post_name(self, post_name):
    self.driver.find_element_by_name('name').send_keys(post_name)


# on posts page create a new post create_a_new_post_dialog
def click_create_submit_button(self):
    self.driver.find_element_by_xpath('//*[contains(text(), "Create") and @type="submit"]').submit()


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
def scroll_to_page_bottom(self):
    js = "document.documentElement.scrollTop=10000"
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
    click_go_back_to_posts_page_button(self)
    wait_until_posts_page_is_visible(self)


# on posts page
def verify_posts_page_have_post(self, post_name):
    assert post_name in self.driver.find_element_by_xpath('//*[contains(text(), ' + "\"" + post_name + "\"" + ')]').text


# on posts page -> edit_post_page -> delete_warning_dialog -> posts_page
def delete_a_post(self, post_name):  # todo: 直接在posts page上delete post
    read_a_post(self, post_name)
    scroll_to_page_bottom(self)
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


# todo: variables post_name
# xpath example:  //*[contains(@id, "listHeaderSortButton")]
class TestPostFeatures(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)

    def test_create_post_on_the_admin_ui_page_successfully(self):
        go_to_posts_page_from_admin_ui_page(self)
        create_a_post(self, 'abc')
        go_back_to_posts_page_from_edit_page(self)
        verify_posts_page_have_post(self, 'abc')

    def tearDown(self) -> None:
        delete_a_post(self, 'abc')
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
