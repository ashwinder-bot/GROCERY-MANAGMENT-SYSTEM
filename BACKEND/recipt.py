class GroceryItem:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

class GroceryManagementSystem:
    def __init__(self):
        self.items = []
        self.customer_name = ""
    
    def add_customer(self):
        self.customer_name = input("Enter the customer's name: ")
        print(f"\nWelcome, {self.customer_name}! You can now add items to your bill.")

    def add_item(self):
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        
        item = GroceryItem(item_name, quantity, price)
        self.items.append(item)
        print(f"{item_name} added successfully!")

    def display_bill(self):
        if not self.items:
            print("No items in the bill yet.")
            return

        print(f"\nBill for {self.customer_name}:")
        print("{:<15} {:<10} {:<10} {:<10}".format("Item Name", "Quantity", "Price", "Total"))
        print("-" * 45)
        
        total_cost = 0
        for item in self.items:
            print("{:<15} {:<10} {:<10} {:<10}".format(item.item_name, item.quantity, item.price, item.total_price))
            total_cost += item.total_price

        print("-" * 45)
        print(f"Total Bill Amount: ${total_cost:.2f}")

    def remove_item(self):
        item_name = input("Enter the name of the item to remove: ")
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"{item_name} removed from the bill.")
                return
        print(f"{item_name} not found in the bill.")

    def exit_bill(self):
        print("\nFinalizing the bill...")
        self.display_bill()
        print("\nThank you for shopping with us!")
        self.items = []  # Clear items after the bill is finalized

def main():
    system = GroceryManagementSystem()
    system.add_customer()

    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Bill")
        print("4. Exit and Finalize Bill")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            system.add_item()
        elif choice == '2':
            system.remove_item()
        elif choice == '3':
            system.display_bill()
        elif choice == '4':
            system.exit_bill()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
