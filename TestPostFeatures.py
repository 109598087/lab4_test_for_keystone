from selenium import webdriver
import unittest


class TestPostFeatures(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('chromedriver.exe')

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.fullscreen_window()

    def test_create_post_on_the_admin_ui_page(self):
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div[2]/a").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
