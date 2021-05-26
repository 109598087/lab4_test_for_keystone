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


def wait_until_sign_in_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "logo")]')


def wait_until_admin_ui_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@class, "dashboard-group")]')


def wait_until_posts_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Create ")]')


def wait_until_edit_post_page_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/posts")]')


def wait_until_comments_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Create ")]')


def wait_until_edit_comment_page_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/post-comments")]')


def wait_until_users_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(text(), "Create ")]')


def wait_until_edie_user_page_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-e2e-editform-header-back, "true") and contains(@href, "/keystone/users")]')


# dialog
def wait_until_create_a_new_post_dialog_is_visible(self):
    wait_until_element_visible_by_name(self, 'name')


def wait_until_delete_warning_dialog(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-button-type, "confirm") and contains(text(), "Delete")]')


def wait_until_reset_warning_dialog(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@data-button-type, "confirm") and contains(text(), "Reset")]')


def wait_until_create_a_new_user_dialog_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[@data-screen-id="modal-dialog"]')


# element
def wait_until_delete_button_on_edit_post_page_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@data-button, "delete")]')


def wait_until_name_error_message_is_visible(self):
    wait_until_element_visible_by_xpath(self, '//*[contains(@data-alert-type, "danger")]')


def wait_until_input_select_is_visible(self):
    wait_until_element_visible_by_xpath(self,
                                        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[contains(@aria-activedescendant, "react-select")]')
