from ShowMessages import typing_print
from ShowMessages import typing_print_emoji
from Utils import string_contains
import Commands

welcome = """Welcome to Quick Market Chatbot Demo
   /)/)
 ( ˶•.•)   Hello My name is Quickie
୭( づ✿)    I'm glad I could assist you.\n"""
typing_print(
    "｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡\n", 0.01)
print(welcome)
Commands.show_commands()

while True:
    command_input = input("\nask: ").lower().strip()

    if command_input.startswith("/help") or string_contains(command_input,  ["help", "how", "tulong", "need help", "guide"]):
        Commands.show_commands()
    elif command_input.startswith("/category"):
        Commands.find_category(command_input)
    elif command_input.startswith("/price"):
        Commands.find_price(command_input)
    elif command_input.startswith("/product"):
        print(command_input)
    elif command_input.startswith("/info"):
        Commands.find_info(command_input)
    # breaking the loop
    elif string_contains(command_input, ["quit", "i want to quit", "abort"]):
        typing_print("[Quitting]\n")
        quitCommand = input("Did you want to quit? \ninput: ").lower().strip()
        if string_contains(quitCommand, ["confirm", "yes", "agree", "y"]):
            typing_print(
                "Thank you for having a conversation.\nAnd Have a great day!")
            break
    else:
        typing_print_emoji(f"Quickie:[{command_input}] are not on the commands"
                           f"\nI can follow and understand please try again")

 # (\__/)
 # (•ㅅ•)
