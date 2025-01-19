import time
import pyautogui
from openpyxl.pivot.fields import Number
from unicodedata import category

pyautogui.PAUSE = 0.5   # increases "0.5" seconds for each command executed

# 1 - Opening Browser
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)   # wait "1" seconds before proceed

# Joining URL
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)   # wait "1" seconds before proceed

# 2 - Login
pyautogui.click(694, 375)
pyautogui.write("your-email@example.com")

pyautogui.press("tab")
pyautogui.write("your-password")

pyautogui.press("tab")  # move to the password field
pyautogui.press("enter")

# 3 - Import products`s databases
import pandas

table = pandas.read_csv("products.csv")
print(table)

time.sleep(1)

# 4 - Register products
pyautogui.PAUSE = 0.1   # increases "0.1" seconds for each command executed
for line in table.index:
    pyautogui.click(747, 259) # click in the first field

    # ID
    id = table.loc[line, "id"]
    pyautogui.write(str(id))
    pyautogui.press("tab")

    # Brand
    brand = table.loc[line, "brand"]
    pyautogui.write(str(brand))
    pyautogui.press("tab")

    # Type
    type = table.loc[line, "type"]
    pyautogui.write(str(type))
    pyautogui.press("tab")

    # Category
    category = table.loc[line, "category"]
    pyautogui.write(str(category))  # str -> string = text
    pyautogui.press("tab")

    # Unit Price
    unit_price = table.loc[line, "unit_price"]
    pyautogui.write(str(unit_price))
    pyautogui.press("tab")

    # Cost
    cost = table.loc[line, "cost"]
    pyautogui.write(str(cost))
    pyautogui.press("tab")

    # Obs
    obs = str(table.loc[line, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.press("home") # move to the top


