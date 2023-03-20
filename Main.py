from CoffeeMachine import MenuItem, Menu, CoffeeMaker, Coins, MoneyMachine

print("Starting Coffee Machine")
print("Loading Menu Item...")
latte = MenuItem("latte", 2.4, {"water": 100, "coffee": 16, "milk":150})
espresso = MenuItem("espresso", 1.5, {"water": 10, "coffee": 20, "milk":0})
cappuccino = MenuItem("cappuccino", 1.9, {"water": 50, "caffee": 15, "milk": 50})
menu = Menu()
menu.add_item(latte)
menu.add_item(espresso)
menu.add_item(cappuccino)

print("Stating Money Machine")
money_machine = MoneyMachine()
money_machine.set_currency("$")

# print(menu.items)
# print(menu.get_items())

print("Loading Ingredients...")
coffee_maker = CoffeeMaker()
coffee_maker.fill_ingredient("water",100)
coffee_maker.fill_ingredient("water",25)
coffee_maker.fill_ingredient("coffee",150)
coffee_maker.fill_ingredient("milk",500)
print(coffee_maker.report()) 
print("""     )))
    (((
  +-----+
  |     |]   My Coffee Machine
  `-----'        (Welcome)
___________
`---------'""")

def input_processor(option: str):
    match option:
        case "menu":
            print(menu.get_items())
        case "off" | "exit" | "quit":
            print("Powering off")
            quit()
        case "order":
            order_item = input(f"What would you like? ({menu.get_items()}): ")
            item_obj = menu.find_drink(order_item)
            if item_obj is not None:
                print(f"You have selected {item_obj.name} which cost {money_machine.currency}{item_obj.cost}")
                if coffee_maker.is_resource_sufficient(item_obj):
                    payment_flag = money_machine.make_payment(item_obj.cost)
                    if payment_flag:
                        print(coffee_maker.make_coffee(item_obj))
            else:
                print("Invalid Coffee Name.")
        case "inventory":
            print(coffee_maker.report())
        case "profit":
            money_machine.report()
        case "help":
            print("Options: menu/order/off")
        case other:
            print("Unknow Option Selected. Please select one of the following option:\nmenu/order/off")

while True:
    option = input("> ")
    input_processor(option)


# print(coffee_maker.is_resource_sufficient(latte))
# print(coffee_maker.make_coffee(latte))

# print(coffee_maker.report())

# money_machine = MoneyMachine()
# money_machine.set_currency("$")
# money_machine.make_payment(2.05)
