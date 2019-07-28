import unittest
from import_module import import_module
site = import_module("Website", "website.py")

class test_when_on_the_index_page(unittest.TestCase):
    def setUp(self):
        self.website = site.WebSite()

    def tearDown(self):
        self.website.quit
        
    def test_the_link_to_step_2_should_work(self):
        step2_title_text = self.website.index().click_link_step2().title_text
        self.assertEqual(step2_title_text, "Udaiyan Protein Predictor - Wizard 2")
    
    def test_changing_the_protein_dropdown_should_update_the_selected_protein(self):
        expected_text = "Protein Sample 3"
        selected_text = self.website.index().select_dropdown_by_text(expected_text).get_selected_protein_text()
        self.assertEqual(selected_text, "Selected: " + expected_text)

if __name__ == '__main__':
    unittest.main()
    