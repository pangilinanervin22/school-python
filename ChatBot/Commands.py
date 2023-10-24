import Storage
from ShowMessages import typing_print


def get_list_category():
    typing_print(f"Quickie: List of available category\n")
    index = 0
    for item in Storage.all_list_category.keys():
        index += 1
        typing_print(f"{index}. {item}\n")


def get_list_product_category(input_command="Seafood"):
    if not Storage.all_list_category.keys().__contains__(input_command):
        typing_print(f"Quickie: Category of {input_command} don't exist\n\n")
        get_list_category()
        return

    typing_print(f"Here are the list of available {input_command}:\n")

    index = 0
    for item in Storage.all_list_category[input_command].values():
        index += 1
        price = item["price"]
        name = item["name"]
        typing_print(f"{index}. {name} - {price}\n")


def find_category(input_commands):
    input_value = input_commands.replace("/category", "").strip().lower()

    if len(input_value) == 0:
        get_list_category()
    else:
        get_list_product_category(input_value)
        typing_print("\n")


def find_price(input_commands):
    input_value = input_commands.replace("/price", "").strip().lower()

    if not Storage.all_list_product.keys().__contains__(input_value):
        typing_print(f"we don't have {input_value}")
        return

    temp = Storage.all_list_product[input_value]
    price = temp.get("price")
    name = temp.get("name")
    typing_print(f"Quickie: Here {name} is only {price} pesos")


def find_info(input_commands):
    input_value = input_commands.replace("/info", "").strip().lower()

    if not Storage.all_list_product.keys().__contains__(input_value):
        typing_print(f"Quickie: we don't have a product called {input_value}")
        return

    temp = Storage.all_list_product[input_value]
    name = temp.get("name")
    price = temp.get("price")
    category = temp.get("category")

    typing_print(f"{name} \n")
    typing_print(f"Category: {category} \n")
    typing_print(f"Price: {price} \n")


def show_commands():
    typing_print(
        "｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n", 0.01)
    typing_print("""Quickie: List of commands that I can understand
Message               Description                           Usage
# /help                - list of commands that available      - /help
# /category @given     - list of product in given category    - /category seafood
# /price @given        - show price of given product          - /price tilapia    
# /info @given         - show information of given product    - /info tilapia
      \n""", 0.001)
    typing_print(
        "｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n", 0.01)


"""
   
"""
