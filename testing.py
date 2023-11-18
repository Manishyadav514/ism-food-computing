from selenium import webdriver

from selenium.webdriver.common.by import By
# Example HTML content
html_content = """
<span class="wprm-recipe-time wprm-block-text-normal">
    <span class="wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-prep_time wprm-recipe-prep_time-minutes">
        15
        <span class="sr-only screen-reader-text wprm-screen-reader-text"> minutes</span>
    </span>
    <span class="wprm-recipe-details-unit wprm-recipe-details-minutes wprm-recipe-prep_time-unit wprm-recipe-prep_timeunit-minutes" aria-hidden="true">minutes</span>
</span>
"""

# Initialize the Selenium WebDriver (in this case, I'm using Chrome)
driver = webdriver.Edge()

# Load HTML content into the WebDriver
driver.get("data:text/html;charset=utf-8," + html_content)

# Find the element by class name
element = driver.find_element(By.CLASS_NAME, "wprm-recipe-prep_time")

# Get the text content of the element
content = element.text

# Print the result
print("Content:", content)

# Close the WebDriver
driver.quit()
