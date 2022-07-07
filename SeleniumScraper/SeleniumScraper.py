# Written by Nathan Spencer

# This simple library provides a basic getting started approach to
# web scraping dynamic websites with Selenium and BeautifulSoup.
#

###################################################
# Imports
#
# webdriver main functionality
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

# additional imports
from bs4 import BeautifulSoup # pip install bs4
#
###################################################


# Enables scraping of dynamic websites using selenium
#
class SeleniumScraper:
    def __init__(self) -> None:
        self.driver = None
        self.__load_strategy = "normal" # accepts "none" and "eager"
        self.__webdriver_data_folder = "webdriver_folder"
        self.__options = Options()
        self.__initialize_driver()


    # Set the basic webdriver options
    #
    def __initialize_driver(self) -> None:
        # set the options
        self.__options.page_load_strategy = self.__load_strategy
        self.__options.add_argument("user-data-dir={}".format(self.__webdriver_data_folder))
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__options)
        
        
    # Use the webdriver to get the specified url
    #
    def get(self, url:str) -> None:
        self.driver.get(url)
        
    
    # Return a BeautifulSoup object of the entire page source from the driver.
    # Call get() before using this method
    #
    def get_soup(self) -> BeautifulSoup:
        soup = BeautifulSoup(self.driver.page_source, features='html.parser')
        return soup


# test code
if __name__ == "__main__":
    driver = SeleniumScraper()
    driver.get("https://pypi.org/project/selenium/")
    soup = driver.get_soup()
    header = soup.find("h1", {"class":"package-header__name"}).text
    if "selenium" in header:
        print("Success")
    else:
        print("Failure")
    