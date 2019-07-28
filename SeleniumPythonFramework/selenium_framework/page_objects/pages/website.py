from selenium import webdriver
from import_module import import_module
site = import_module("Index", "index.py")
        
class WebSite:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Darren\github\SeleniumPythonFramework\selenium_framework\drivers\chromedriver.exe")
        self.driver.get(r"http://localhost/protein/")
        
    def index(self):
        return site.Index(self.driver)

    def quit(self):
        self.driver.quit()

