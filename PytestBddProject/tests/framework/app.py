import os, time
from selenium import webdriver
import allure
from selenium.webdriver import Keys

class APP:
    vl_delay = 20
    l_delay = 10
    m_delay = 5
    s_delay = 3
    vs_delay = 2

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self._driver = webdriver.Chrome(options=options)
        #self._driver = webdriver.Chrome()

    @property
    def driver(self):
        return self._driver

    def take_screenshot(self, folder):
        name = ''
        name = folder.rsplit('/', 1)[1] if '/' in folder else folder
        
        save_location = "tests/report/screenshots/{}/".format(folder)
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        timestr = time.strftime("%Y%m%d_%H-%M-%S")
        full_path = '{}/{} {}.png'.format(path, name, timestr)

        self._driver.set_window_size(1368, 768)
        time.sleep(0.3)
        self._driver.get_screenshot_as_file(full_path)
        self._driver.maximize_window()

    def navigate_to_url(self, url):
        with allure.step(f"Navigate to the given URL({str(url)})"):
            self.driver.get(url)

    def get_element(self, element):
        with allure.step(f"Get the element with the given locator({element})"):
            return self.driver.find_element(*element)

    def input_text(self, element, value, is_to_clear=True):
        with allure.step(f"Entering the given value({value}) in the text field"):
            self.wait_for_element_presence(element)
            self.scroll_to_an_element(element)
            if is_to_clear:
                self.get_element(element).send_keys(Keys.CONTROL + "a")
                self.get_element(element).send_keys(Keys.DELETE)
            self.get_element(element).send_keys(value)

    def send_enter_key(self, element):
        with allure.step(f"Entering the Keyboard Enter Key on the given element({element})"):
            self.verify_element_presence(element)
            self.get_element(element).send_keys(Keys.ENTER)

    def get_text(self, element):
        with allure.step(f"Get the text attribute value from the given element({element})"):
            self.wait_for_element_presence(element)
            return self.get_element(element).text

    def get_property_value(self, element_locator, property_name):
        with allure.step(f"Get the given property value from the given element({element_locator})"):
            return self.get_element(element_locator).get_property(property_name)
        
    def find_and_click_an_element(self, element, element_gone=False, validate_element_visible=None):
        with allure.step(f"Click on the given element({element})"):
            self.get_element(element).click()
            if element_gone:
                self.verify_absence_of_an_element(element)
            if validate_element_visible is not None:
                self.verify_element_on_page(validate_element_visible)

    def get_text(self, element):
        with allure.step(f"Get the text attribute value from the given element({element})"):
            self.wait_for_element_presence(element)
            return self.get_element(element).text