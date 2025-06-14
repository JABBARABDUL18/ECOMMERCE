import tkinter as tk
from tkinter import messagebox

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Smartphone", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 800},
    {"id": 5, "name": "Mouse", "price": 500}
]

cart = []

# Function to add product to cart
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Cart", f"{product['name']} added to cart!")

# Function to show the cart
def show_cart():
    cart_window = tk.Toplevel(window)
    cart_window.title("Your Cart")
    
    total = 0
    for item in cart:
        label = tk.Label(cart_window, text=f"{item['name']} - ₹{item['price']}")
        label.pack()
        total += item['price']
    
    total_label = tk.Label(cart_window, text=f"Total: ₹{total}", font=("Arial", 12, "bold"))
    total_label.pack(pady=10)
    
    checkout_btn = tk.Button(cart_window, text="Checkout", command=lambda: checkout(total, cart_window))
    checkout_btn.pack(pady=5)

# Function to simulate checkout
def checkout(total, cart_window):
    if not cart:
        messagebox.showwarning("Cart Empty", "Add products to your cart before checkout.")
    else:
        messagebox.showinfo("Order Placed", f"Your order of ₹{total} has been placed successfully!")
        cart.clear()
        cart_window.destroy()

# Main window
window = tk.Tk()
window.title("Simple E-Commerce Store")
window.geometry("400x400")

title = tk.Label(window, text="Welcome to Our Store", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Product listing
for product in products:
    frame = tk.Frame(window)
    frame.pack(pady=5)
    
    name = tk.Label(frame, text=f"{product['name']} - ₹{product['price']}", width=25, anchor="w")
    name.pack(side="left")
    
    add_btn = tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
    add_btn.pack(side="right")

# Show Cart Button
cart_btn = tk.Button(window, text="View Cart", command=show_cart, bg="blue", fg="white")
cart_btn.pack(pady=20)

window.mainloop()
