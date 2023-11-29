from selenium import webdriver
from selenium.webdriver.common.by import By

def get_element_text(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        text = element.text if element else ""
        return text
    except Exception as e:
        print(f"Error getting element text: {e}")
        return ""

driver = webdriver.Edge()

driver.get(
    "https://www.vegrecipesofindia.com/paneer-butter-masala/#h-ingredients-you-need"
)

try:
    # Extract Cuisine, Course, Diet, Difficulty Level
    cuisine = get_element_text(driver, "//span[@class='wprm-recipe-cuisine']")
    course = get_element_text(driver, "//span[@class='wprm-recipe-course']")
    diet = get_element_text(driver, "//span[@class='wprm-recipe-suitablefordiet']")
    difficulty = get_element_text(driver, "//span[@class='wprm-recipe-difficulty']")
    # Extract Prep Time, Cook Time, Total Time
    prep_time = get_element_text(driver, "//span[@class='wprm-recipe-prep_time']")
    cook_time = get_element_text(driver, "//span[@class='wprm-recipe-cook_time']")
    total_time = get_element_text(driver, "//span[@class='wprm-recipe-total_time']")

    print("Cuisine:", cuisine)
    print("Course:", course)
    print("Diet:", diet)
    print("Difficulty Level:", difficulty)
    print("Prep Time:", prep_time)
    print("Cook Time:", cook_time)
    print("Total Time:", total_time)

finally:
    driver.quit()
