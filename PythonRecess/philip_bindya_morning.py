import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

class Shoe:
    def __init__(self, name, price):
        self.name = name
        self.price = price

shoes = [
    Shoe("Sneakers", 150000),
    Shoe("Loafers", 100000),
    Shoe("Boots", 250000),
    Shoe("Sandals", 20000),
    Shoe("Oxfords", 300000),
    Shoe("Flip Flops", 60000),
    Shoe("Heels", 130000),
    Shoe("Running Shoes", 50000)
]

def calculate_total():
    selected_shoes = []
    total_price = 0.0
    for i, var in enumerate(var_list):
        if var.get() == 1:
            selected_shoes.append(shoes[i].name)
            total_price += shoes[i].price

    if selected_shoes:
        receipt = "Selected Shoes:\n"
        for shoe in selected_shoes:
            receipt += "- " + shoe + "\n"
        receipt += "Total Price: UGX," + str(total_price)

        messagebox.showinfo("Receipt", receipt)
    else:
        messagebox.showwarning("No Selection", "Please select at least one shoe.")

root = tk.Tk()
root.title("Shoe Store")

# Custom Fonts
title_font = Font(family="Helvetica", size=16, weight="bold")
label_font = Font(family="Helvetica", size=12)
button_font = Font(family="Helvetica", size=14, weight="bold")

# Colors
bg_color = "#E0F4F9"  # Light blue background
title_color = "blue"
button_color = "#0077CC"  # Dark blue button color
price_color = "white"

# Set Background Color
root.configure(bg=bg_color)

var_list = []

# Title Label
title_label = tk.Label(root, text="Shoe Store", font=title_font, bg=bg_color, fg=title_color)
title_label.pack(pady=10)

for shoe in shoes:
    var = tk.IntVar()
    var_list.append(var)
    checkbutton = tk.Checkbutton(root, text=shoe.name + " (UGX," + str(shoe.price) + ")", variable=var, font=label_font, bg=bg_color, fg=title_color, selectcolor=bg_color, activebackground=bg_color, activeforeground=title_color)
    checkbutton.pack(anchor=tk.W)

button = tk.Button(root, text="Calculate Total", command=calculate_total, font=button_font, bg=button_color, fg="white")
button.pack(pady=20)

root.mainloop()
