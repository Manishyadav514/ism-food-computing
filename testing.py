import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom


# class FoodComputing:
#     def __init__(self):
#         self.driver = webdriver.Edge()
#         self.driver.get("https://www.vegrecipesofindia.com/paneer-butter-masala/")
#         self.driver.implicitly_wait(5)

#     def run_all(self):
#         try:
#             page_source = self.driver.page_source
#             tree = ET.HTML(page_source)
#             tree.write("output.xml", pretty_print=True)

#         except Exception as e:
#             print(f"Error: {e}")

#         finally:
#             self.driver.quit()

#     def prettify(self, elem):
#         rough_string = tostring(elem, "utf-8")
#         reparsed = minidom.parseString(rough_string)
#         return reparsed.toprettyxml(indent="  ")

#     def action(self):
#         root = Element("recipes")

#         recipe = SubElement(root, "recipe")
#         recipe_title = SubElement(recipe, "recipeTitle")
#         recipe_title.text = ""  # Assign an empty string for now

#         website_content = SubElement(recipe, "website_content")
#         website_content.text = ""  # Assign an empty string for now

#         # Extract and add the title
#         title_element = self.driver.find_element(By.XPATH, "//h1")
#         recipe_title.text = title_element.text

#         # Extract and add the content of various tags in order
#         # Extract and add the content of various tags in order
#         elements = self.driver.find_elements(
#             By.XPATH,
#             "//*[self::h1 or self::h2 or self::h3 or self::p or self::ul or self::span or self::li]",
#         )
#         for element in elements:
#             tag_name = element.tag_name
#             tag = SubElement(website_content, tag_name)
#             tag.text = element.text

#         with open("website_content_selenium.xml", "w", encoding="utf-8") as file:
#             file.write(self.prettify(root))

#         self.driver.quit()


# if __name__ == "__main__":
#     analyzer = FoodComputing()
#     analyzer.action()


class FoodComputing:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.vegrecipesofindia.com/paneer-butter-masala/")
        self.driver.implicitly_wait(5)

    # def run_all(self):
    #     try:
    #         page_source = self.driver.page_source
    #         tree = ET.HTML(page_source)
    #         tree.write("output.xml", pretty_print=True)

    #     except Exception as e:
    #         print(f"Error: {e}")

    #     finally:
    #         self.driver.quit()

    def preittifyContent(self, elem):
        rough_string = tostring(elem, "utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def getWholeWebContent(self):
        root = Element("recipes")

        recipe = SubElement(root, "recipe")
        recipe_title = SubElement(recipe, "recipeTitle")
        recipe_title.text = ""  # Assign an empty string for now

        website_content = SubElement(recipe, "website_content")
        website_content.text = ""  # Assign an empty string for now

        # Extract and add the title
        title_element = self.driver.find_element(By.XPATH, "//h1")
        recipe_title.text = title_element.text

        # Extract and add the content of various tags in order
        elements = self.driver.find_elements(
            By.XPATH,
            "//*[self::h1 or self::h2 or self::h3 or self::p or self::ul or self::span or self::li]",
        )
        for element in elements:
            tag_name = element.tag_name
            tag_text = element.text.strip()  # Remove leading/trailing white spaces
            if tag_text:  # Check if the content is not empty
                tag = SubElement(website_content, tag_name)
                tag.text = tag_text

        with open("website_content_selenium.xml", "w", encoding="utf-8") as file:
            file.write(self.preittifyContent(root))

        self.driver.quit()


if __name__ == "__main__":
    analyzer = FoodComputing()
    analyzer.getWholeWebContent()
