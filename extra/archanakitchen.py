from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget
import csv
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET


# Set the path to your webdriver executable (e.g., Chrome or Edge)
# driver = webdriver.Edge()
# url = "https://www.archanaskitchen.com/index.php?option=com_akrecipes&lang=en&limit=24&limitstart=312&view=frontpage"
html_content = """
<div class="row recipeingredientsanddirections">
<div class="col-md-4 col-12 recipeingredients">
<h2 class="ingredientstitle">Ingredients</h2>
<ul class="list-unstyled">
<b class="ingredientssubtitle">Ingredients to make the Onion Medu Vada</b>
<li itemprop="ingredients">
1 cup <span class="ingredient_name" data-original-title="" title="">White Urad Dal
(Whole)</span> , (soaked for 3 hours) </li>
<li itemprop="ingredients">
1 inch <span class="ingredient_name" data-original-title="" title="">Ginger</span> </li>
<li itemprop="ingredients">
1 <span class="ingredient_name" data-original-title="" title="">Green Chillies</span> , chopped
</li>
<li itemprop="ingredients">
<span class="ingredient_name" data-original-title="" title="">Salt</span> , to taste
</li>
<li itemprop="ingredients">
2 <span class="ingredient_name" data-original-title="" title="">Onions</span> , finely chopped
</li>
<li itemprop="ingredients">
1/4 <span class="ingredient_name" data-original-title="" title="">Coriander (Dhania)
Leaves</span> , finely chopped </li>
<li itemprop="ingredients">
<span class="ingredient_name" data-original-title="" title="">Oil</span> , for pan frying
</li>
<b class="ingredientssubtitle">Ingredients for Vengaya Sambar</b>
<li itemprop="ingredients">
1 cup <span class="ingredient_name" data-original-title="" title="">Arhar dal (Split Toor
Dal)</span> </li>
<li itemprop="ingredients">
1/2 cup <span class="ingredient_name" data-original-title="" title="">Pearl onions (Sambar
Onions)</span> </li>
<li itemprop="ingredients">
1 <span class="ingredient_name" data-original-title="" title="">Mooli/ Mullangi (Radish)</span>
, chopped </li>
<li itemprop="ingredients">
1 <span class="ingredient_name" data-original-title="" title="">Carrot (Gajjar)</span> , chopped
</li>
<li itemprop="ingredients">
1-1/2 cups <a target="_blank"
href="https://www.archanaskitchen.com/video-recipe-how-to-make-homemade-tamarind-water"><span
class="ingredient_name" data-original-title="" title="">Tamarind Water</span></a> </li>
<li itemprop="ingredients">
2 teaspoons <a target="_blank" href="https://www.archanaskitchen.com/sambar-powder-podi"><span
class="ingredient_name" data-original-title="" title="">Sambar Powder</span></a> </li>
<li itemprop="ingredients">
<span class="ingredient_name" data-original-title="" title="">Salt</span> , to taste
</li>
<li itemprop="ingredients">
<span class="ingredient_name" data-original-title="" title="">Coriander (Dhania) Leaves</span> ,
a small bunch chopped
</li>
<b class="ingredientssubtitle">For Seasoning of Sambar</b>
<li itemprop="ingredients">
1 teaspoon <span class="ingredient_name" data-original-title="" title="">Gingelly oil</span>
</li>
<li itemprop="ingredients">
1/2 teaspoon <span class="ingredient_name" data-original-title="" title="">Mustard seeds (Rai/
Kadugu)</span> </li>
<li itemprop="ingredients">
2 <span class="ingredient_name" data-original-title="" title="">Dry Red Chillies</span> </li>
<li itemprop="ingredients">
1 sprig <span class="ingredient_name" data-original-title="" title="">Curry leaves</span> </li>
<li itemprop="ingredients">
1/4 teaspoon <span class="ingredient_name" data-original-title="" title="">Asafoetida
(hing)</span> </li>
</ul>
</div>
<!-- recipe inline ad 1 -->
<div class="col-md-8 col-12 recipeinstructions">
<h2 class="recipeinstructionstitle">How to make Mini Onion Vada With Vengaya Sambar Recipe - Pan
Fried Fritters in Tangy Lentil Curry </h2>
<ol>
<li itemprop="recipeInstructions">
<p>To begin making the Onion Vada Sambar Recipe; &nbsp;we will first soak the dal for about 3
hours.</p>
</li>
<li itemprop="recipeInstructions">
<p>Using a strainer, strain all the excess water from the&nbsp;urad&nbsp;dal. We need to use
very little water to grind the&nbsp;urad&nbsp;dal,&nbsp;so that you can shape them well if you
are deep frying.</p>
</li>
<li itemprop="recipeInstructions">
<p>Next we will grind the dal, along with ginger and green chillies using a food processor or a
mixer grinder into a very smooth batter. Make sure add very little water while grinding the
dal to make a smooth batter. Transfer the batter to a bowl.&nbsp;</p>
</li>
<li itemprop="recipeInstructions">
<p>Add in the chopped onions, coriander leaves into the batter. Stir well to combine the
ingredients well into the vada batter.</p>
</li>
<li itemprop="recipeInstructions">
<p>Next we will preheat the&nbsp;Kuzhi&nbsp;Paniyaram&nbsp;Pan and add in a little oil into each
cavity; once the pan is&nbsp;well heated&nbsp;spoon the mini onion vada mixture into each of
the cavities. Cover the pan and allow it to steam until you notice that the top looks
cooked.&nbsp;</p>
</li>
<li itemprop="recipeInstructions">
<p>After a couple minutes of steaming of&nbsp;notice&nbsp;the top part of the mini onion
vada&nbsp;looks cooked. At this&nbsp;point&nbsp;you could add a little more oil and then flip
the&nbsp;vada&nbsp;so it can get cooked and crisp from both sides. This time, allow it to cook
without the cover.&nbsp;</p>
</li>
<li itemprop="recipeInstructions">
<p>Transfer the Mini Onion Vadas&nbsp;to a platter and continue the same process with the
remaining batter.</p>
</li>
<li itemprop="recipeInstructions">
<p>To make the Vengaya Sambar recipe, pressure cook the toor dal along with 2 cups of water for
3 to 4 whistles and turn off the heat. Once the pressure releases naturally, open the cooking
and mash the toor dal until soft. Keep aside.</p>
</li>
<li itemprop="recipeInstructions">
<p>Into a pressure cooker; add the tamarind water, onions, radish, carrot, sambar powder and
salt. Pressure cook for 2 whistles and turn off the heat.</p>
</li>
<li itemprop="recipeInstructions">
<p>Add the cooker toor dal into the sambar water and bring to a brisk boil. Adjust the
consistency by adding a little water if required.</p>
</li>
<li itemprop="recipeInstructions">
<p>In a small tadka pan, heat oil over medium heat. Add mustard seeds and red chillies and allow
it to crackle. Stir in the asafoetida and curry leaves. Pour this over the simmering vengaya
sambar. Check the salt and spices of the vengaya sambar and adjust to suit your taste. Once
done, turn off the heat , stir in the chopped coriander leaves and serve.&nbsp;</p>
</li>
<li itemprop="recipeInstructions">
<p>To serve the Onion Vada Sambar, place the&nbsp;vadas&nbsp;in a bowl or a platter, pour in
some Vengaya Sambar&nbsp;and sprinkle some chopped onions and serve hot.</p>
</li>
</ol>
</div>
</div> 
"""
# Set the path to your webdriver executable (e.g., Chrome or Edge)
driver = webdriver.Edge()
# data = []


class Flipkart:
    data = []

    def __init__(self):
        # Load the webpage
        # driver.get(url)  # Replace 'your_webpage_url' with the actual URL
        # Load the HTML content into the webdriver
        driver.get("data:text/html;charset=utf-8," + html_content)

        # Maximize the browser window
        driver.maximize_window()
        # wait = WebDriverWait(driver, 10)

    def loadDataOnEachPage(self):
        self.data = []
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
            self.data.append([food_title, author_name, image_url, recipe_url])

    def nextButtonClick(self):
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
            return True
        else:
            return False  # here are some changes

    def saveDataInCSV2(data):
        # Save the data to a CSV file
        csv_filename = "food_data.csv"
        with open(csv_filename, mode="w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the header row
            csv_writer.writerow(
                ["Food Title", "Author Name", "Image URL", "Recipe URL"]
            )

            # Write the data rows
            csv_writer.writerows(data)

        print(f"Data saved to {csv_filename}")

    def saveDataInCSV(self):
        try:
            csv_filename = "food_data.csv"

            # Check if the file already exists
            file_exists = os.path.exists(csv_filename)

            with open(csv_filename, "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)

                # Write the data rows
                if not file_exists:
                    # If the file is new, write the header row
                    csv_writer.writerow(
                        ["Food Title", "Author Name", "Image URL", "Recipe URL"]
                    )

                # Write the data rows
                csv_writer.writerows(self.data)
            print(f"Data saved to {csv_filename, len( self.data)}")
        except Exception:
            print("not found")

    def getBlogData(self):
        try:
            # Wait for the elements to be present (modify as needed)
            driver.find_element(By.CLASS_NAME, "recipeinstructionstitle")
            driver.find_element(By.XPATH, "//li[@itemprop='recipeInstructions']/p")

            # Create an XML document
            root = ET.Element("recipe")

            # Extract recipe title
            title_element = driver.find_element(
                By.CLASS_NAME, "recipeinstructionstitle"
            )
            recipe_title = title_element.text if title_element else "No Title"

            # Create title element in XML
            title_xml_element = ET.SubElement(root, "title")
            title_xml_element.text = recipe_title

            # Extract recipe instructions
            instructions_elements = driver.find_elements(
                By.XPATH, "//li[@itemprop='recipeInstructions']/p"
            )
            if instructions_elements:
                instructions_xml_element = ET.SubElement(root, "instructions")
                for instruction_element in instructions_elements:
                    instruction_text = instruction_element.text.strip()
                    ET.SubElement(
                        instructions_xml_element, "step"
                    ).text = instruction_text

            # Save XML to a file
            tree = ET.ElementTree(root)
            tree.write("recipe_data.xml", encoding="utf-8", xml_declaration=True)


            # Wait for the elements to be present (modify as needed)


            # # Create an XML document
            # root = ET.Element("recipe")

            # # Extract Ingredients
            # ingredients_section = driver.find_element(By.CLASS_NAME, "recipeingredients")
            # ingredients_xml_element = ET.SubElement(root, "ingredients")
            # ingredient_title_element = ingredients_section.find_element(By.CLASS_NAME, "ingredientstitle")
            # ingredient_title = ingredient_title_element.text if ingredient_title_element else "No Title"
            # title_xml_element = ET.SubElement(ingredients_xml_element, "title")
            # title_xml_element.text = ingredient_title

            # ingredients_elements = ingredients_section.find_elements(By.XPATH, "//li[@itemprop='ingredients']")
            # if ingredients_elements:
            #     ingredients_list_xml_element = ET.SubElement(ingredients_xml_element, "ingredients_list")
            #     current_subtitle = None
            #     for ingredient_element in ingredients_elements:
            #         if ingredient_element.get_attribute("class") == "ingredientssubtitle":
            #             current_subtitle = ingredient_element.text.strip()
            #         else:
            #             ingredient_text = ingredient_element.text.strip()
            #             ET.SubElement(ingredients_list_xml_element, "ingredient", subtitle=current_subtitle).text = ingredient_text

            # # Extract Instructions
            # instructions_section = driver.find_element(By.CLASS_NAME, "recipeinstructions")
            # instructions_xml_element = ET.SubElement(root, "instructions")
            # instructions_title_element = instructions_section.find_element(By.CLASS_NAME, "recipeinstructionstitle")
            # instructions_title = instructions_title_element.text if instructions_title_element else "No Title"
            # title_xml_element = ET.SubElement(instructions_xml_element, "title")
            # title_xml_element.text = instructions_title

            # instructions_elements = instructions_section.find_elements(By.XPATH, "//li[@itemprop='recipeInstructions']")
            # if instructions_elements:
            #     instructions_list_xml_element = ET.SubElement(instructions_xml_element, "instructions_list")
            #     for instruction_element in instructions_elements:
            #         instruction_text = instruction_element.text.strip()
            #         ET.SubElement(instructions_list_xml_element, "instruction").text = instruction_text

            # # Save XML to a file
            # tree = ET.ElementTree(root)
            # tree.write("recipe_data.xml", encoding='utf-8', xml_declaration=True)



        except Exception:
            print("not found")


if __name__ == "__main__":
    flipkart = Flipkart()
    # while True:
    #     # Extract data from the current page
    #     flipkart.loadDataOnEachPage()
    #     flipkart.saveDataInCSV()
    #     print(driver.current_url)
    #     if not flipkart.nextButtonClick():
    #         break

    # # flipkart.saveDataInCSV()
    # print("Task completed")
    flipkart.getBlogData()
