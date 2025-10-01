import json
import pyautogui, time
import pyperclip

raw = json.load(open("dump.json"))

recipies = {}

prompt = """Please convert the below text into a json format where each ingredient is stored like:
[{"Name": "...", "Quantity": ...}, ... ]
If the quantity value will not go well in the format 'Quantity' x 'Name', then set it to a empty string if it will work
Only response with the output in a ```json``` format.
Do not response with any other text:
"""


def parse_ingredients(raw):
    full_prompt = prompt + raw

    pyautogui.click(x=1048, y=969)
    time.sleep(0.5)

    pyperclip.copy(full_prompt)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.hotkey("enter")
    time.sleep(10)

    pyautogui.click(x=1089, y=904)
    time.sleep(1)

    pyautogui.click(x=1419, y=154)
    time.sleep(0.5)

    return eval(pyperclip.paste())



time.sleep(5)

for raw_recipe in raw:
    ingredients = []

    recipie = {
      "Servings": raw_recipe["servings"],
      "TimeToCookInMins": 0,
      "Ingredients": parse_ingredients(raw_recipe["ingredients_text_raw"]),
      "Description": "No Description",
      "HowToMake": raw_recipe["recipe_text"],
      "isGlutenFree": True
    }

    recipies[raw_recipe["title"]] = recipie

    json.dump(recipies, open("recipies_processing.json", "w"))


#json.dump(recipies, open("recipies_processed.json", "w"))
