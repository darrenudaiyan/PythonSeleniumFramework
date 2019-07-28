from selenium import webdriver
from import_module import import_module
site = import_module("Step2", "step2.py")
drop_down = import_module("DropDown", "drop_down.py")


class Index():
    def __init__(self, webDriver):
        self.driver = webDriver
        self.page_name = "/index.html"
        self.link_step2 = self.driver.find_element_by_id("LinkStep2")
        self.title_text = self.driver.title
        self.protein_options = self.driver.find_element_by_id("ProteinOptions")
        self.dropdown = drop_down.DropDown(self.driver, self.protein_options)
        
    
    def click_link_step2(self):
        self.link_step2.click()
        return site.Step2(self.driver)
    
    def select_dropdown_by_text(self, byText):
        self.dropdown.change_drop_down_value(byText)
        return self
    
    def get_selected_protein_text(self):
        selected_protein = self.driver.find_element_by_id("SelectedProtein")
        return selected_protein.text