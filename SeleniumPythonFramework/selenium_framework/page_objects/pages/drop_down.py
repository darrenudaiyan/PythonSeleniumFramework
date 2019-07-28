from selenium import webdriver
from selenium.webdriver.support.ui import Select

class DropDown():
    def __init__(self, webDriver, webElement):
        self.driver = webDriver
        self.element = webElement
        
    def change_drop_down_value(self, byText):
        select_element = Select(self.element)
        select_element.select_by_value(byText)
