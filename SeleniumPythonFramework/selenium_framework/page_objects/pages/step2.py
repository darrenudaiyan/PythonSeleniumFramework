from selenium import webdriver

class Step2():
    def __init__(self, webDriver):
        self.driver = webDriver
        self.page_name = "/step2.html"
        self.link_step3 = self.driver.find_element_by_id("LinkStep3")
        self.title_text = self.driver.title
    
    def click_link_step3(self):
        self.link_step3.click()