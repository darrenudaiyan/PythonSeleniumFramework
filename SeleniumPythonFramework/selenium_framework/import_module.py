import importlib.util

def import_module(module_name, module_path):
    pages_path = r"C:/Darren/github/SeleniumPythonFramework/selenium_framework/page_objects/pages/"
    spec = importlib.util.spec_from_file_location(module_name, pages_path + module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
