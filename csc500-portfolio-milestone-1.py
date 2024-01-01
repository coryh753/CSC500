class ItemToPurchase:
    def __init__(self, itemName = "none", itemPrice = 0, itemQuantity = 0):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
    
    def calculateTotalOfItem(self):
        return(self.itemQuantity * self.itemPrice)
    
    def printItemToPurchase(self):
        return(f"{self.itemName} {self.itemQuantity} @ ${self.itemPrice} = ${self.calculateTotalOfItem()}")

try:    
    userInputItemName1 = input("Please enter the name of the first item: ")
    userInputItemQuantity1 = int(input("How many of this item? "))
    userInputItemPrice1 = float(input("What is the price of the item? "))

    userInputItemName2 = input("Please enter the name of the first item: ")
    userInputItemQuantity2 = int(input("How many of this item? "))
    userInputItemPrice2 = float(input("What is the price of the item? "))

    newItem = ItemToPurchase(userInputItemName1, userInputItemPrice1, userInputItemQuantity1)
    newItem2 = ItemToPurchase(userInputItemName2, userInputItemPrice2, userInputItemQuantity2)

    print("Total Cost:")
    print(newItem.printItemToPurchase())
    print(newItem2.printItemToPurchase())
    print(f"Total: ${newItem.calculateTotalOfItem() + newItem2.calculateTotalOfItem()}")

except ValueError:
    print("Hey, check that input")