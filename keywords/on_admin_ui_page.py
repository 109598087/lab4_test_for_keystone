# on admin_ui_page
def click_a_dashboard_button(self, heading, label):
    self.driver.find_element_by_xpath(
        '//*[contains(@data-section-label,' + heading + ')]//*[contains(@class, "dashboard-group__list-label") and text()=' + "\"" + label + "\"" + ']').click()

