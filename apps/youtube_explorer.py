# Written By Nathan Spencer

# This demo app shows the SeleniumScraper libraries utility by scraping the 
# explore feed from youtube.com
#

from selenium.webdriver.common.by import By
import time
import sys

# import the project
sys.path.insert(0, "SeleniumScraper")
from SeleniumScraper import SeleniumScraper


# client code to get all the videos from the youtube explore feed
if __name__ == "__main__":
    # set up the scraper
    driver = SeleniumScraper()
    
    # request the youtube explore feed
    driver.get("https://www.youtube.com/feed/explore")
    
    # get the soup from the library
    soup = driver.get_soup()
    
    # test to make sure the header isnt a cookie test...
    h1 = soup.find("h1")
    if h1 is not None:
        text = h1.text
        if text == "Before you continue to YouTube":
            reject_element = driver.driver.find_element(By.CSS_SELECTOR, "button[jsname='tWT92d']")
            reject_element.click()
            time.sleep(1)
            soup = driver.get_soup()
            
    # use the soup to parse each video
    videos = soup.find_all("ytd-video-renderer", {"class":"style-scope ytd-expanded-shelf-contents-renderer"})
    for video in videos:
        # get the video main info
        title_element = video.find("a", {"id":"video-title"})
        link = title_element.attrs['href']
        title = title_element.text
        
        # get the video meta info
        meta_line = video.find("div", {"id":"metadata-line"})
        meta_elements = meta_line.find_all("span")
        views = meta_elements[0].text
        posted_time = meta_elements[1].text
        
        # get the channel info
        channel_element = video.find("div", {"id":"byline-container"}).find("a")
        channel_name = channel_element.text
        channel_link = channel_element.attrs['href']
        
        # print the info to the screen
        print("Title: " + title)
        print("Video URL: " + link)
        print("Views: " + views)
        print("Posted Time: " + posted_time)
        print("Channel Name: " + channel_name)
        print("Channel URL: " + channel_link)
    pass