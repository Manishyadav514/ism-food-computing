import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET


class FoodComputing:
    def __init__(self, url):
        self.driver = webdriver.Edge()
        self.url = url

    def load_json_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                classes = json.load(file)
            return classes
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

    def get_middle_part(self, url):
        # Split the URL by dots
        parts = url.split(".")

        # Extract the middle part (second-to-last part)
        middle_part = parts[-2] if len(parts) >= 2 else url
        return middle_part

    # analyze_url function retunrs obj class from differentiator.json for that particular url
    def analyze_url(self, identifier_file_path):
        middle_part = self.get_middle_part(self.url)
        print("url key:", middle_part)

        json_data = self.load_json_file(identifier_file_path)
        if json_data and middle_part in json_data:
            return json_data[middle_part]
        else:
            print(f"No identifier found for '{middle_part}'")
            return None

    # save all blog content in xml file
    # def save_to_xml(self, title_text):
    #     xml_file = "foodData.xml"
    #     try:
    #         tree = ET.parse(xml_file)
    #         root = tree.getroot()
    #     except FileNotFoundError:
    #         # If the file doesn't exist, create a new XML structure
    #         root = ET.Element("recipes")
    #         tree = ET.ElementTree(root)

    #     recipe = ET.SubElement(root, "recipe")
    #     recipe_title = ET.SubElement(recipe, "recipeTitle")
    #     recipe_title.text = title_text

    #     tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    def save_to_xml(self, title_text, prepTime):
        xml_file = "foodData.xml"
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
        except FileNotFoundError:
            # If the file doesn't exist, create a new XML structure
            root = ET.Element("recipes")
            tree = ET.ElementTree(root)

        # Create a dictionary for the elements
        elements = {"recipeTitle": title_text, "prepTime": prepTime}

        # Add elements to the XML
        recipe = ET.SubElement(root, "recipe")
        for element, text in elements.items():
            sub_element = ET.SubElement(recipe, element)
            sub_element.text = text

        tree.write(xml_file, encoding="utf-8", xml_declaration=True)

    def get_blog_data(self, identifier_obj):
        try:
            title_element = self.driver.find_element(
                By.CLASS_NAME, identifier_obj["recipeTitle"]
            )
            prepTime_element = self.driver.find_element(
                By.CLASS_NAME, identifier_obj["prep_time"]
            )
            # Extract the title text
            title_text = title_element.text
            prepTime_text = prepTime_element.text

            # Print the title
            print("\nTitle:", title_text)
            print("\nPrep Time:", prepTime_text)
            return title_text, prepTime_text

        except Exception as e:
            print(f"Error: {e}")

    def run_analysis(self, identifier_file_path):
        try:
            self.driver.get(self.url)
            identifier_obj = self.analyze_url(identifier_file_path)

            if identifier_obj:
                title_text, prepTime_text = self.get_blog_data(identifier_obj)
                if title_text:
                    self.save_to_xml(title_text, prepTime_text)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.driver.quit()


url_list = [
    "https://www.vegrecipesofindia.com/paneer-butter-masala/",
    "https://www.archanaskitchen.com/jalapeno-potato-cheese-balls-recipe-with-four-pepper-cheese-dip",
    "https://www.indianhealthyrecipes.com/paneer-butter-masala-restaurant-style/",
]

if __name__ == "__main__":
    for url in url_list:
        print("\nAnalyzing URL:", url)
        analyzer = FoodComputing(url)
        # analyzer.save_to_xml(url)
        analyzer.run_analysis("differentiator.json")
