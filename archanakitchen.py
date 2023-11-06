from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import csv

# Set the path to your webdriver executable (e.g., Chrome or Edge)
# driver = webdriver.Edge()
url = "https://www.archanaskitchen.com/"

# Set the path to your webdriver executable (e.g., Chrome or Edge)
driver = webdriver.Edge()
data = []


class Flipkart:
    def __init__(self):
        # Load the webpage
        driver.get(url)  # Replace 'your_webpage_url' with the actual URL
        # Maximize the browser window
        driver.maximize_window()
        # wait = WebDriverWait(driver, 10)

    def loadDataOnEachPage(self):
        # Find all elements with the specified structure
        elements = driver.find_elements(
            By.XPATH, "//div[@class='ak_frontpage_item mb-2 col-md-3']"
        )
        print("Food Items on page 1:", len(elements))

        # Loop through the found elements and extract the desired information
        for element in elements:
            # Extract the image URL
            try:
                image_element = element.find_element(
                    By.XPATH, ".//div[@class='recipe-image']//img"
                )
                image_url = image_element.get_attribute("src")
            except Exception:
                image_url = "no-image"
            # Extract the food title
            try:
                food_title_element = element.find_element(
                    By.XPATH, ".//a[@class='recipe-title']//span[@itemprop='name']"
                )
                food_title = food_title_element.text
            except Exception:
                food_title = "no-title"
            # Extract the author name
            try:
                author_element = element.find_element(
                    By.XPATH, ".//span[@itemprop='author']"
                )
                author_name = author_element.text
            except Exception:
                author_name = "no-author"
            # Extract the URL
            try:
                url_element = element.find_element(
                    By.XPATH, ".//a[@class='recipe-title']"
                )
                recipe_url = url_element.get_attribute("href")
            except Exception:
                recipe_url = "no-url"
            # Print the extracted information
            # Append the data to the list
            data.append([food_title, author_name, image_url, recipe_url])

    # def nextButtonClick():
    #     # Find all "a" elements within "li" elements with the class 'page-item'
    #     buttons = driver.find_elements(By.XPATH, "//li[contains(@class, 'page-item')]//a")
    #     next_button = next(button for button in buttons if button.text == "Next")
    #     next_button.click()
    def saveDataInCSV(self):
        # Save the data to a CSV file
        csv_filename = "food_data.csv"

        with open(csv_filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the header row
            csv_writer.writerow(
                ["Food Title", "Author Name", "Image URL", "Recipe URL"]
            )

            # Write the data rows
            csv_writer.writerows(data)

        print(f"Data saved to {csv_filename}")


if __name__ == "__main__":
    Flipkart = Flipkart()
    while True:
        # Extract data from the current page
        Flipkart.loadDataOnEachPage()
        # Find and click the button with text "Next" if it exists
        next_button = next(
            (
                button
                for button in driver.find_elements(
                    By.XPATH, "//li[contains(@class, 'page-item')]//a"
                )
                if button.text == "Next"
            ),
            None,
        )

        if next_button:
            next_button.click()
        else:
            break
    Flipkart.saveDataInCSV()
    print("Task completed")
