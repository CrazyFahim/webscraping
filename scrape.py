import time
import datetime
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Links 

def scrape_page(date, url, sleepTime):
    # Create the URL by combining the prefixURL and the date
    url = ''.join([url+'/date/'+str(date.date())])

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(Links.PATH_TO_DRIVER)

    # Navigate to the specified URL
    driver.get(url)

    # Wait for all tables on the page to be present
    tables = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table")))

    # Introduce a sleep time to avoid errors
    time.sleep(sleepTime)

    # Read the HTML tables into a list of dataframes
    a = pd.read_html(tables[1].get_attribute('outerHTML'))
     
    # Select the first dataframe
    df=a[0]

    # Drop rows with NaN values in the 'Time' column
    df = df[df['Time'].notna()] 

    # Insert the 'Date' column
    df.insert(0, 'Date', date, allow_duplicates=True)
    #print(df) # for print and chek if the code works

    # Write the dataframe to a CSV file, appending to the existing file
    df.to_csv(r'data.csv', index = False, columns=['Date','Time','Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.','Condition'], mode='a', header=None)

    # Quit the WebDriver
    driver.quit()

if __name__ == "__main__":
    # Specify the date and url of wunderground
    date = datetime.datetime(2023,9,13)
    prefixURL = Links.url1
    
    scrape_page(date,prefixURL,sleepTime=3)
