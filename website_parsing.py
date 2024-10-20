# Import the necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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

for container in containers:
    title = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/span').text
    subtitle = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/h3').text

    link = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a').get_attribute("href")



