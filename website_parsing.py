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

# At this point, 'containers' will hold a list of all matching elements from the page
