from dataclasses import dataclass
from enum import Enum

@dataclass
class MenuItem:
    name: str
    cost: float
    ingredients: dict
    
class Menu:
    
    items = []
    
    def add_item(self, item: MenuItem):
        self.items.append(item)
    
    def get_items(self) -> str:
        item_names = [item.name for item in self.items]
        return "/".join(item_names)
    
    def find_drink(self, order_name: str) -> MenuItem:
        for item in self.items:
            if item.name == order_name:
                return item
        return None
        
class CoffeeMaker:
    
    ingredients = {}
    
    """
    Should I have Ingredient a object here?
    """

    def fill_ingredient(self, ingredient: str, quantity: int) -> None:
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
            
    
    def report(self) -> str:
        report_str = ""
        for ingredient in self.ingredients:
            report_str += f"{ingredient}: {self.ingredients[ingredient]}\n"
        return report_str
    
    def is_resource_sufficient(self, drink: MenuItem) -> str:
        for ingredient in drink.ingredients:
            if ingredient in self.ingredients:
                if self.ingredients[ingredient] < drink.ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    return False
            else:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True
    
    def make_coffee(self, order: MenuItem) -> str:
        for ingredient in order.ingredients:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] -= order.ingredients[ingredient]
        return "Here is your Latte. Enjoy!"

class Coins(Enum):
    quaters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

class MoneyMachine:
    currency = None
    machine_balance = 0

    def set_currency(self, currency: str) -> None:
        self.currency = currency
        print(f"Currency set to {self.currency}")

    def add_balance(self, amount: float) -> None:
        prev_balance = self.machine_balance
        self.machine_balance += amount
        print(f"Amount added machine balance:\nBefore: {prev_balance}\nAfter: {self.machine_balance}")

    def report(self) -> None:
        print(f"Money: {self.machine_balance}")

    def make_payment(self, cost: float):
        coins_str = input(f"Insert Coins as CSV: ")
        coins_str = coins_str.split(",")
        coins_split = [coin.strip() for coin in coins_str]
        coins_value = 0.0
        print(f"You have inserted following coins: ")
        for coin_class in coins_split:
            coin_class_split = coin_class.split(" ")
            coin_class_total = int(coin_class_split[0]) * Coins[coin_class_split[1]].value
            coins_value += coin_class_total
            print(f"{coin_class_split[0]} X {coin_class_split[1]} = {coin_class_split[0]} X {self.currency}{Coins[coin_class_split[1]].value} = {self.currency}{coin_class_total}")
        print(f"Total Coin Value: {self.currency}{coins_value}")

        diff = coins_value - cost

        if diff < 0:
            print(f"Sorry that's not engough money. Money refunded.")
            return False
        elif diff > 0:
            print(f"Here is {self.currency}{round(diff,2)} in change.")
        
        self.machine_balance += cost
        return True 
            
    