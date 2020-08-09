import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import requests
import json

def main():
    
    # Build Chrome Webdriver
    chrome_options = Options()
    # Toggle Headless Option On/Off here:
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    print("Running...")
    
    # Enter Search Query
    print("Please enter search query: ")
    query = input().lower()
    print("Searching for " + query)
    query.replace(" ","+")

    # Perform Search
    browser.get("https://www.google.com/search?q="+query+"&source=lnms&tbm=isch")
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    
    # Create Storage Folder
    if not os.path.exists(query):
        os.mkdir(query)
    os.chdir(query)
    print("Directory Created")

    # Scroll Far Enough To Load Sufficient Number of Images
    for _ in range(1000):
        browser.execute_script("window.scrollBy(0,100000)")
    # Click the "Show more results" Button
    browser.find_elements_by_class_name("mye4qd")[0].click()
    for _ in range(1000):
        browser.execute_script("window.scrollBy(0,100000)")
    print("Scrolling Complete")

    # Find Each Image Thumbnail
    counter = 0
    succounter = 0
    for x in browser.find_elements_by_css_selector(".wXeWr.islib.nfEiy.mM5pbd"):
        counter = counter + 1
        print("Total Count: ", counter)
        
        try:
            # Find Each Image URL, and Download
            x.click()
            y = browser.find_elements_by_class_name("n3VNCb")
            imgURL = y[0].get_attribute("src")
            print("Image URL: ",imgURL)
            
            urllib.request.urlretrieve(imgURL, str(succounter)+".jpg")
            succounter = succounter + 1

            print("Successful Count: ", succounter)
        except:
            print("Can't download image.")

    print(counter, "pictures attempted")
    print(succounter, "pictures succesfully downloaded")
    
    browser.quit()
    print("Complete")
    return 0

if __name__ == "__main__":
    main()