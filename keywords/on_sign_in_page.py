# on sign_in_page
def input_email(self):
    self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')


# on sign_in_page
def input_password(self):
    self.driver.find_element_by_name('password').send_keys('demo')


# on sign_in_page -> admin_ui_page
def submit_email_and_password(self):
    self.driver.find_element_by_xpath('//*[contains(@type, "submit") and contains(text(), "Sign In")]').submit()


# on sign_in_page
def click_logo_button(self):
    self.driver.find_element_by_xpath('//*[contains(@class, "logo")]').click()
