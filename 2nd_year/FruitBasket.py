basket = []
totalFruit = int(input("Input the number of total fruit: "))

print("Enter fruit what to store \n"
                + "A/a for apple \n"
                + "O/o for orange \n"
                + "M/m for melon \n"
                + "G/g for grapes \n")

def inputFruit(input):
    if input == "a":
        basket.append("apple")
    elif input == "o":
        basket.append("orange")
    elif input == "m":
        basket.append("melon")
    elif input == "g":
        basket.append("grapes")
    else:
        basket.append("random")

for i in range(totalFruit):
    fruit = input(f"Fruit {i + 1} of {totalFruit}: ").lower()
    inputFruit(fruit)

print(f"Your basket have: {basket}")

while len(basket) != 1:
    eatCommand = input("Press E to eat the a fruit: ").lower()
    if(eatCommand ==  "e"):
        basket.pop()
        print(f"Fruit in the basket: {basket}")

input("Press E to eat the a fruit: ").lower()
print("No more fruit to eat")

