import time

from selenium import webdriver
import unittest

from keywords.wait_until_is_visible import wait_until_home_page_is_visible


class TestEnquirieCreate(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('../chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.maximize_window()
        wait_until_home_page_is_visible(self)

    def test_create_enquirie(self):
        self.driver.find_element_by_xpath('//*[@href="/contact"]').click()
        enquirie_first_name = "chu"
        enquirie_email = "t109598087@ntut.org.tw"
        enquirie_message = "enquirie_message"
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="form-control" and @name="name.full"]').send_keys(
            enquirie_first_name)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="form-control" and @name="email"]').send_keys(enquirie_email)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="form-control" and @name="enquiryType"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@value="message" and text()="Just leaving a message"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="form-control" and @name="enquiryType"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="form-control" and @name="message"]').send_keys(enquirie_message)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[contains(@class, "btn") and text()="Submit"]').submit()
        time.sleep(2)
        assert "Success!" in self.driver.find_element_by_tag_name('h1').text
        print("TestEnquiryCreate ok")

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
