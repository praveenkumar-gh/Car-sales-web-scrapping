from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Selenium WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# URL to scrape
driver.get('https://www.examplecarwebsite.com/cars-for-sale')

car_data = []

# Waiting for the page to load
time.sleep(5)

# Extracting car listings
cars = driver.find_elements(By.CSS_SELECTOR, 'div.car-listing')
for car in cars:
    make = car.find_element(By.CSS_SELECTOR, 'span.make').text
    model = car.find_element(By.CSS_SELECTOR, 'span.model').text
    price = car.find_element(By.CSS_SELECTOR, 'span.price').text
    year = car.find_element(By.CSS_SELECTOR, 'span.year').text
    url = car.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    
    car_data.append({
        'make': make,
        'model': model,
        'price': price,
        'year': year,
        'url': url
    })

# Saving the data to a JSON file
with open('cars.json', 'w') as f:
    json.dump(car_data, f, indent=4)

driver.quit()