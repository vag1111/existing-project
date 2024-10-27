# Import the necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")
# Define the URL of the website we want to scrape
website = "https://www.thesun.co.uk/sport/football/"

# Specify the path to the ChromeDriver executable
path = "/Users/victoraviles/Desktop/existing-project/chromedriver-mac-x64/chromedriver"

# Create a Service object with the specified path to the ChromeDriver
service = Service(executable_path=path)

# Initialize a new instance of the Chrome WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Use the WebDriver to navigate to the specified website
driver.get(website)

# Find all elements on the page that match the specified XPath
# In this case, we are looking for div elements with the class 'teaser__copy-container'
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
data_headlines = []  # **Added this list to capture data-headline**

for container in containers:
    try:
        # Extract the title text
        title = container.find_element(by="xpath", value='.//a/span').text
        
        # Extract the subtitle text
        subtitle = container.find_element(by="xpath", value='.//a/h3').text
        
        # Extract the link (href attribute)
        link = container.find_element(by="xpath", value='.//a').get_attribute("href")
        
        # **Extract the data-headline attribute**
        data_headline = container.find_element(by="xpath", value='.//a').get_attribute("data-headline")
        
        # Append the extracted values to their respective lists
        titles.append(title)
        subtitles.append(subtitle)  
        links.append(link)
        data_headlines.append(data_headline)  # **Append the data-headline to the list**

    except Exception as e:  # **Catch exceptions to avoid breaking the loop**
        print(f"Error extracting data from container: {e}")

# Create a dictionary to hold the data
my_dict = {'Titles': titles, 'Subtitle': subtitles, 'Link': links, 'Data Headline': data_headlines}  # **Added Data Headline to dictionary**

# Convert the dictionary to a DataFrame
df_headlines = pd.DataFrame(my_dict)
# Define the file name
file_name = f'Headline - {month_day_year}.csv'
# Create the full path to save the file
final_path = os.path.join(app_path, file_name)

# Export the DataFrame to a CSV file with index=false
df_headlines.to_csv(final_path, index=False)

# Close the WebDriver session
driver.quit()  # Ensure to call quit() properly
