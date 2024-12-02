import tkinter as tk
from tkinter import messagebox, filedialog
import csv


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

    def add_customer(self, name):
        self.customer_name = name

    def add_item(self, item_name, quantity, price):
        item = GroceryItem(item_name, quantity, price)
        self.items.append(item)

    def generate_receipt(self):
        total = sum(item.total_price for item in self.items)
        receipt = f"Customer: {self.customer_name}\n\nItems:\n"
        for item in self.items:
            receipt += f"{item.item_name} (x{item.quantity}): ${item.total_price:.2f}\n"
        receipt += f"\nTotal: ${total:.2f}"
        return receipt

def create_gui():
    system = GroceryManagementSystem()


    root = tk.Tk()
    root.title("Grocery Management System")
    root.geometry("600x400")

    tk.Label(root, text="Customer Name:").grid(row=0, column=0, pady=5, padx=5, sticky="e")
    customer_name_entry = tk.Entry(root)
    customer_name_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

    tk.Label(root, text="Item Name:").grid(row=1, column=0, pady=5, padx=5, sticky="e")
    item_name_entry = tk.Entry(root)
    item_name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="w")

    tk.Label(root, text="Quantity:").grid(row=2, column=0, pady=5, padx=5, sticky="e")
    quantity_entry = tk.Entry(root)
    quantity_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

    tk.Label(root, text="Price per Unit:").grid(row=3, column=0, pady=5, padx=5, sticky="e")
    price_entry = tk.Entry(root)
    price_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")


    items_listbox = tk.Listbox(root, width=50, height=10)
    items_listbox.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

   
    def add_customer():
        name = customer_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Customer name cannot be empty!")
            return
        system.add_customer(name)
        messagebox.showinfo("Success", f"Customer '{name}' added!")
        customer_name_entry.config(state="disabled")

    def add_item():
        name = item_name_entry.get().strip()
        quantity = quantity_entry.get().strip()
        price = price_entry.get().strip()

        if not (name and quantity and price):
            messagebox.showerror("Error", "All item fields must be filled!")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and price a number!")
            return

        system.add_item(name, quantity, price)
        items_listbox.insert(tk.END, f"{name} (x{quantity}) - ${price * quantity:.2f}")
        item_name_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    def generate_receipt():
        if not system.items:
            messagebox.showerror("Error", "No items added!")
            return

        receipt = system.generate_receipt()
        receipt_window = tk.Toplevel(root)
        receipt_window.title("Receipt")
        receipt_text = tk.Text(receipt_window, width=50, height=20)
        receipt_text.insert(tk.END, receipt)
        receipt_text.config(state="disabled")
        receipt_text.pack()

    def save_receipt_as_csv():
        if not system.items:
            messagebox.showerror("Error", "No items added!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Save Receipt as CSV"
        )
        if not file_path:
            return

        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Customer Name", system.customer_name])
                writer.writerow([])
                writer.writerow(["Item Name", "Quantity", "Price per Unit", "Total Price"])
                for item in system.items:
                    writer.writerow([item.item_name, item.quantity, item.price, item.total_price])
                total = sum(item.total_price for item in system.items)
                writer.writerow([])
                writer.writerow(["Total", "", "", total])
            messagebox.showinfo("Success", f"Receipt saved as '{file_path}'")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save receipt: {e}")


    tk.Button(root, text="Add Customer", command=add_customer).grid(row=0, column=2, pady=5, padx=5)
    tk.Button(root, text="Add Item", command=add_item).grid(row=3, column=2, pady=5, padx=5)
    tk.Button(root, text="Generate Receipt", command=generate_receipt).grid(row=4, column=2, pady=5, padx=5)
    tk.Button(root, text="Save as CSV", command=save_receipt_as_csv).grid(row=5, column=2, pady=5, padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
