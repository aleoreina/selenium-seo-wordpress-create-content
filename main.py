# Selenium Content Generator

# Python Natives
import time

# Selenium Driver
from selenium import webdriver

#Selenium Elements
from selenium.webdriver.common.keys import Keys

# Selenium Exceptions
from selenium.common.exceptions import NoSuchElementException

class Selenium_Manager :
    
    def __init__ (self) :
        self.driver = webdriver.Firefox()
        
    def go_url (self, **kwargs):

        try:
            self.driver.get(kwargs.pop('url'))
        except :
            print  ("Cannot acced to this page.")

    def xpath_click() :
        pass

    def xpath_input_text(self, element, text, Enter=False) :
        if isinstance(element, list) :
            for item in element :
                try:
                    target = self.driver.find_element_by_xpath(item)
                    time.sleep(1)
                    try:
                        target.clear()
                    except:
                        pass
                    if (Enter == True) :
                        import pdb; pdb.set_trace()
                        target.send_keys(text + Keys.RETURN)
                    else :
                        target.send_keys(text)
                    return True
                except NoSuchElementException:
                    continue

            return False

    def refresh() :
        pass


class Automaticweb  :

    SearchYoutubeInput = list()
    SearchYoutubeInput.append('//*[@name="search_query"]')

    def __init__ (self, **kwargs):
        try :
            self.url = kwargs.pop('url')
        except :
            print ("No url sended")
        try:
            self.controller = kwargs.pop('web')
        except:
            print ("No webdriver sended.")

    def start(self, **kwargs):
        data = kwargs.get('data')
        self.get_from_youtube(data)

    def go_wp_create_content (youtube=False) :
        self.controller.go_url ()

    def get_from_youtube(self, data):
        # Go page
        self.controller.go_url(url="https://youtube.com/")
        # Input search
        self.controller.xpath_input_text(self.SearchYoutubeInput, , True)


Web = Selenium_Manager()
Plugin_AutoWeb = Automaticweb(url="https://localhost/", web=Web)
data = "SEO" #Must be a list (PENDING TO UPDATE)
Plugin_AutoWeb.start(data=data)
