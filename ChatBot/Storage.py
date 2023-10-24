import Product

all_list_category = {
    "beverage":  Product.FruitList,
    "fruit": Product.FruitList,
    "personal care": Product.PersonalCareList,
    "meat": Product.MeatList,
    "seafood": Product.SeafoodList,
    "vegetable": Product.VegetableList,
}

all_list_product = {
    **Product.FruitList,
    **Product.VegetableList,
    **Product.PersonalCareList,
    **Product.SeafoodList,
    **Product.BeverageList,
    **Product.CondimentsList,
    **Product.MeatList,
}
