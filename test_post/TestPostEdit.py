import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys

from TestPostCreate import sign_in_as_admin, go_to_posts_page_from_admin_ui_page, create_a_post, delete_a_post, \
    go_back_to_home_page_from_sign_in_page, sign_out
from keywords.wait_until_is_visible import wait_until_home_page_is_visible, wait_until_input_select_is_visible, \
    wait_until_reset_warning_dialog, wait_until_edit_post_page_is_visible


def click_post_state_select_arrow(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[@class = "Select-arrow"]').click()


def input_select_post_state(self, post_state):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(post_state)


def click_post_author_select_arrow(self):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[@class = "Select-arrow"]').click()


def input_select_post_author(self, post_author):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[contains(@aria-activedescendant, "react-select")]') \
        .send_keys(post_author)


def click_save_button(self):
    self.driver.find_element_by_xpath('//*[@data-button = "update"]').click()


def click_reset_changes_button(self):
    self.driver.find_element_by_xpath('//*[@data-button="reset"]').click()


##############################################################################################
def input_post_state(self, post_state):
    click_post_state_select_arrow(self)  # todo: need wait?
    input_select_post_state(self, post_state)
    input_select_post_state(self, Keys.ENTER)


def input_post_author(self, post_author):  # todo: 仍有可能錯
    click_post_author_select_arrow(self)
    wait_until_input_select_is_visible(self)
    time.sleep(2)  # todo: wait
    input_select_post_author(self, post_author)
    time.sleep(2)  # todo: wait
    input_select_post_author(self, Keys.ENTER)


def input_post_published_date(self, post_published_date):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="publishedDate"]//*[@name = "publishedDate"]').send_keys(
        Keys.CONTROL, 'a')
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="publishedDate"]//*[@name = "publishedDate"]').send_keys(
        post_published_date)
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="publishedDate"]//*[@name = "publishedDate"]').send_keys(
        Keys.ENTER)
    # for leave published date todo: need better way?
    self.driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_DOWN)
    self.driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_UP)


def input_post_content_brief(self, post_content_brief):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.brief"]//*[contains(@id, "keystone-html")]').send_keys(
        Keys.CONTROL, 'a')
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.brief"]//*[contains(@id, "keystone-html")]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.brief"]//*[contains(@id, "keystone-html")]').send_keys(
        post_content_brief)


def input_post_content_extended(self, post_content_extended):
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.extended"]//*[contains(@id, "keystone-html")]').send_keys(
        Keys.CONTROL, 'a')
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.extended"]//*[contains(@id, "keystone-html")]').send_keys(
        Keys.BACKSPACE)
    self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="content.extended"]//*[contains(@id, "keystone-html")]').send_keys(
        post_content_extended)


def save_edit_post(self):
    click_save_button(self)


def verify_edit_post_successfully(self):
    assert 'Your changes have been saved successfully' in self.driver.find_element_by_xpath(  # todo: 包起來
        '//*[@data-alert-type = "success"]').text


def verify_edit_post_state_successfully(self, post_state):
    assert post_state in self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[@class="Select-value-label"]').text


def verify_edit_post_author_successfully(self, post_author):
    assert post_author in self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="author"]//*[@class="Select-value-label"]').text


def verify_edit_post_published_date_successfully(self, post_published_date):
    assert post_published_date in self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="publishedDate"]//*[@name="publishedDate"]').get_attribute(
        'value')  # todo: [contains(@class, "css-1wrt3l9") 可不用contains?


def verify_edit_post_content_brief_successfully(self, post_content_brief):
    self.driver.switch_to.frame(0)
    assert post_content_brief in self.driver.find_element_by_xpath('//*[@id="tinymce"]').text
    self.driver.switch_to.default_content()


def verify_edit_post_content_extended_successfully(self, post_content_extended):
    self.driver.switch_to.frame(1)
    assert post_content_extended in self.driver.find_element_by_xpath('//*[@id="tinymce"]').text
    self.driver.switch_to.default_content()


# on reset dialog
def click_reset_button(self):
    self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]').click()


def edit_post_reset_changes(self):
    click_reset_changes_button(self)
    wait_until_reset_warning_dialog(self)
    click_reset_button(self)
    wait_until_edit_post_page_is_visible(self)


def verify_reset_post_state_successfully(self, post_state):
    assert post_state in self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="state"]//*[@class="Select-value-label"]').text


def verify_reset_post_author_successfully(self, post_author):
    assert post_author not in self.driver.find_element_by_xpath(
        '//*[@class="Select-value-label" and text()=' + post_author + ']').text


def verify_reset_post_published_date_successfully(self, post_published_date):
    assert post_published_date in self.driver.find_element_by_xpath(
        '//*[contains(@class, "css-1wrt3l9") and @for="publishedDate"]//*[@name="publishedDate"]').get_attribute(
        'value')  # todo: [contains(@class, "css-1wrt3l9") 可不用contains?


def verify_reset_post_content_brief_successfully(self, post_content_brief):
    self.driver.switch_to.frame(0)
    assert post_content_brief in self.driver.find_element_by_xpath('//*[@id="tinymce"]').text
    self.driver.switch_to.default_content()


def verify_reset_post_content_extended_successfully(self, post_content_extended):
    self.driver.switch_to.frame(1)
    assert post_content_extended in self.driver.find_element_by_xpath('//*[@id="tinymce"]').text
    self.driver.switch_to.default_content()


def verify_edit_post_fail_with_wrong_published_date(self):
    assert 'PublishedDate is invalid' in self.driver.find_element_by_xpath('//*[@data-alert-type="danger"]//*').text


class TestPostEdit(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)
        sign_in_as_admin(self)
        go_to_posts_page_from_admin_ui_page(self)
        post_name = 'abc'
        create_a_post(self, post_name)

    def test_edit_post_with_ISP_input1(self):
        post_state = 'Draft'
        post_author = 'Demo User'
        post_published_date = '2020-05-20'  # todo: error日期
        post_content_brief = ''
        post_content_extended = ''
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input2(self):
        post_state = 'Published'
        post_author = 'Demo User'
        post_published_date = '2020-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief'
        post_content_extended = 'post_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input3(self):
        post_state = 'Archived'
        post_author = 'Demo User'
        post_published_date = '2021-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_test'
        post_content_extended = 'post_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input4(self):
        post_state = 'Published'
        post_author = 'Demo User'
        post_published_date = '2020-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = ''
        post_content_extended = 'post_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input5(self):
        post_state = 'Archived'
        post_author = 'Demo User'
        post_published_date = '2020-05-20'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_test'
        post_content_extended = 'post_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input6(self):
        post_state = 'Draft'
        post_author = 'Demo User'
        post_published_date = '2021-05-20'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief'
        post_content_extended = 'post_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extendedpost_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input7(self):
        post_state = 'Archived'
        post_author = 'Demo User'
        post_published_date = '2020-05-20'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief'
        post_content_extended = 'post_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input8(self):
        post_state = 'Draft'
        post_author = 'Demo User'
        post_published_date = '2020-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_test'
        post_content_extended = 'post_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input9(self):
        post_state = 'Published'
        post_author = 'Demo User'
        post_published_date = '2022-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = ''
        post_content_extended = 'post_content_extended'
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input10(self):
        post_state = 'Published'
        post_author = 'Demo User'
        post_published_date = '2022-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_testpost_content_brief_test'
        post_content_extended = ''
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    def test_edit_post_with_ISP_input11(self):
        post_state = 'Archived'
        post_author = 'Demo User'
        post_published_date = '2021-05-25'  # todo: error日期  # todo: today_button
        post_content_brief = 'post_content_brief'
        post_content_extended = ''
        input_post_state(self, post_state)
        input_post_author(self, post_author)
        input_post_published_date(self, post_published_date)
        input_post_content_brief(self, post_content_brief)
        input_post_content_extended(self, post_content_extended)
        save_edit_post(self)
        verify_edit_post_successfully(self)
        verify_edit_post_state_successfully(self, post_state)
        verify_edit_post_author_successfully(self, post_author)
        verify_edit_post_published_date_successfully(self, post_published_date)
        verify_edit_post_content_brief_successfully(self, post_content_brief)
        verify_edit_post_content_extended_successfully(self, post_content_extended)
        print('test_edit_post_with_ISP_input ok')

    # def test_edit_post_and_reset_changeds(self):
    #     post_state = 'Archived'
    #     post_author = 'Demo User'
    #     post_published_date = '2021-05-25'  # todo: error日期  # todo: today_button
    #     post_content_brief = 'post_content_brief'
    #     post_content_extended = 'post_content_extended'
    #     input_post_state(self, post_state)
    #     input_post_author(self, post_author)
    #     input_post_published_date(self, post_published_date)
    #     input_post_content_brief(self, post_content_brief)
    #     input_post_content_extended(self, post_content_extended)
    #     edit_post_reset_changes(self)
    #     scroll_page(self, 0)
    #     time.sleep(2)
    #     verify_reset_post_state_successfully(self, 'Draft')
    #     # verify_reset_post_author_successfully(self, post_author)  # todo: how to verify
    #     verify_reset_post_published_date_successfully(self, '2021-05-25')
    #     verify_reset_post_content_brief_successfully(self, '')
    #     verify_reset_post_content_extended_successfully(self, '')
    #     print('test_edit_post_and_reset_changeds ok')

    def test_edit_post_with_wrong_published_date(self):
        post_published_date = 'abc'  # todo: error日期  # todo: today_button
        input_post_published_date(self, post_published_date)
        save_edit_post(self)
        verify_edit_post_fail_with_wrong_published_date(self)
        print('test_edit_post_with_wrong_published_date ok')

    def tearDown(self) -> None:
        post_name = 'abc'
        # go_back_to_posts_page_from_edit_page(self)  # todo: 要移除? todo:要加wait?
        self.driver.back()  # todo: 要移除?
        delete_a_post(self, post_name)
        sign_out(self)
        go_back_to_home_page_from_sign_in_page(self)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
