from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_element_visible_by_xpath(self, xpath):
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))


def wait_until_element_visible_by_name(self, name):
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, name)))


# page
def wait_until_home_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Sign in") and @href="/keystone/signin"]')


def wait_until_admin_ui_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "dashboard-group")]')


def wait_until_posts_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Create ")]')


def wait_until_edit_post_page_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/posts")]')


# dialog
def wait_until_sign_in_dialog_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "logo")]')


def wait_until_create_a_new_post_dialog_is_visible(self):
    wait_until_element_visible_by_name(self, 'name')


def wait_until_delete_warning_dialog(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]')


# element
def wait_until_delete_button_on_edit_post_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@data-button, "delete")]')
