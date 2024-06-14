import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk  

class InventorySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventoria")

        # Background image
        self.background_image = Image.open("Forest.jpg")
        self.background_image = self.background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Label to hold the background image
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Set font
        self.custom_font = font.Font(family="Century Gothic", size=10)

        # Window resize function
        self.root.rowconfigure(4, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)

        # Define the UI components
        self.create_widgets()

        # Inventory data storage
        self.inventory = []

    def create_widgets(self):
        # Title with scrolling effect
        self.canvas = tk.Canvas(self.root, height=40, bg='white')  # Add bg color to canvas for better visibility
        self.canvas.grid(row=0, column=0, columnspan=5, pady=20, padx=30, sticky='ew')
        self.text_id = self.canvas.create_text(0, 20, text="Inventory System - Ariel Clemence Arcangel Prado", font=("Century Gothic", 20), anchor='w')
        self.canvas.update_idletasks()  # Ensure the canvas is updated to get its width
        self.scroll_text()

        # Search Bar, Add Button, and Remove Button
        search_label_frame = tk.Frame(self.root, bg="white")
        search_label_frame.grid(row=1, column=0, pady=5, padx=(30, 0), sticky='w')

        search_entry_frame = tk.Frame(self.root, bg="white")
        search_entry_frame.grid(row=1, column=0, pady=5, padx=(120, 0), sticky='w')

        tk.Label(search_label_frame, text="Search Item", font=self.custom_font, bg="white").pack(side='left')

        self.search_entry = tk.Entry(search_entry_frame, font=self.custom_font, width=50)  
        self.search_entry.pack(side='left')
        self.search_entry.bind("<KeyRelease>", self.search_item)

        # Separate frames for Add and Delete buttons
        add_button_frame = tk.Frame(self.root, bg="white")
        add_button_frame.grid(row=1, column=3, padx=(300, 0), pady=5, sticky='e')

        self.add_button = tk.Button(add_button_frame, text="Add +", bg="#36AE7C", fg="white", font=self.custom_font, width=20, command=self.add_item_form)
        self.add_button.pack(side="left") 

        remove_button_frame = tk.Frame(self.root, bg="white")
        remove_button_frame.grid(row=1, column=4, padx=(5, 30), pady=5, sticky='e')

        self.remove_button = tk.Button(remove_button_frame, text="Delete -", bg="#EB5353", fg="white", font=self.custom_font, width=20, command=self.remove_item)
        self.remove_button.pack(side="left")

        # Product List Label
        tk.Label(self.root, text="Product List", font=("Century Gothic", 16), bg="white").grid(row=2, column=0, pady=10, padx=(30, 0), sticky='w')

        # Product List Table
        self.product_list_frame = tk.Frame(self.root, bg='white')
        self.product_list_frame.grid(row=3, column=0, columnspan=5, padx=30, pady=10, sticky='nsew')

        headers = ["", "Serial Number", "Name", "Qty.", "Price", "Details", "Actions"]
        col_widths = [5, 15, 25, 10, 20, 25, 20]
        for col, (header, width) in enumerate(zip(headers, col_widths)):
            anchor = 'center' if header == "Select" else 'w'
            tk.Label(self.product_list_frame, text=header, borderwidth=0, relief="solid", width=width, anchor=anchor, font=self.custom_font, bg=self.product_list_frame.cget('bg')).grid(row=0, column=col, sticky='ew')

        self.product_list_frame.columnconfigure(0, weight=1)
        for col in range(1, len(headers)):
            self.product_list_frame.columnconfigure(col, weight=1)

        self.product_list = []

    def scroll_text(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.text_id)
        if x2 < 0:  
            self.canvas.coords(self.text_id, self.canvas.winfo_width(), 20)  
        else:
            self.canvas.move(self.text_id, -2, 0)  
        self.root.after(30, self.scroll_text)

    def search_item(self, event):
        query = self.search_entry.get().lower()
        self.refresh_product_list(query)

    def add_item_form(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Item")

        tk.Label(self.add_window, text="Serial Number", font=self.custom_font).grid(row=0, column=0, padx=10, pady=5)
        self.serial_entry = tk.Entry(self.add_window, font=self.custom_font)
        self.serial_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.add_window, text="Name", font=self.custom_font).grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.add_window, font=self.custom_font)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.add_window, text="Quantity", font=self.custom_font).grid(row=2, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.add_window, font=self.custom_font)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.add_window, text="Price", font=self.custom_font).grid(row=3, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.add_window, font=self.custom_font)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.add_window, text="Details", font=self.custom_font).grid(row=4, column=0, padx=10, pady=5)
        self.details_entry = tk.Entry(self.add_window, font=self.custom_font)
        self.details_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.add_window, text="Add", font=self.custom_font, command=self.add_item).grid(row=5, column=0, columnspan=2, pady=10)

    def add_item(self):
        serial = self.serial_entry.get()
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        details = self.details_entry.get()

        if serial and name and quantity and price and details:
            if any(item[0] == serial for item in self.inventory):
                messagebox.showwarning("Warning", "Serial number already exists")
            else:
                self.inventory.append((serial, name, int(quantity), float(price), details))
                self.add_window.destroy()
                self.refresh_product_list()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields")

    def remove_item(self):
        selected_indexes = [i for i, v in enumerate(self.product_list) if v.get()]
        if selected_indexes:
            for index in reversed(selected_indexes):
                del self.inventory[index]
            self.refresh_product_list()
        else:
            messagebox.showwarning("Warning", "No item selected to remove")

    def refresh_product_list(self, query=""):
        for widget in self.product_list_frame.winfo_children()[7:]:
            widget.destroy()

        self.product_list = []
        filtered_inventory = [item for item in self.inventory if query in item[0].lower() or query in item[1].lower()]

        for i, item in enumerate(filtered_inventory):
            self.product_list.append(tk.BooleanVar())
            tk.Checkbutton(self.product_list_frame, variable=self.product_list[-1], bg=self.product_list_frame.cget('bg')).grid(row=i+1, column=0, sticky='ew')

            col_widths = [15, 25, 10, 15, 30, 20]
            for j, (value, width) in enumerate(zip(item, col_widths)):
                label = tk.Label(self.product_list_frame, text=value, borderwidth=0, relief="solid", width=width, anchor='w', font=self.custom_font, bg=self.product_list_frame.cget('bg'))
                label.grid(row=i+1, column=j+1, sticky='ew')
                label.bind("<Button-1>", lambda e, i=i: self.show_item_summary(filtered_inventory[i]))  # Bind click event to each label

            # Frame for action buttons
            action_frame = tk.Frame(self.product_list_frame, bg=self.product_list_frame.cget('bg'))
            action_frame.grid(row=i+1, column=6, sticky='ew')

            original_index = self.inventory.index(item)  # Index in the original inventory list
            update_button = tk.Button(action_frame, text="Update", font=self.custom_font, bg="#187498", fg="white", command=lambda i=original_index: self.edit_item(i))
            update_button.pack(side='left', fill='x', expand=True)  # Fill the horizontal space

            delete_button = tk.Button(action_frame, text="Delete", font=self.custom_font, bg="#EB5353", fg="white", command=lambda i=original_index: self.delete_item(i))
            delete_button.pack(side='left', fill='x', expand=True)  # Fill the horizontal space
            
            action_frame.columnconfigure(0, weight=1)

    def show_item_summary(self, item):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Item Summary")

        summary_text = f"Serial Number: {item[0]}\nName: {item[1]}\nQuantity: {item[2]}\nPrice: ₱{item[3]:,.2f}\nDetails: {item[4]}"
        tk.Label(summary_window, text=summary_text, font=self.custom_font, justify="left", padx=100, pady=40).pack()

    def edit_item(self, index):
        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Edit Item")

        item = self.inventory[index]

        tk.Label(self.edit_window, text="Serial Number", font=self.custom_font).grid(row=0, column=0, padx=10, pady=5)
        self.serial_entry_edit = tk.Entry(self.edit_window, font=self.custom_font)
        self.serial_entry_edit.insert(0, item[0])
        self.serial_entry_edit.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.edit_window, text="Name", font=self.custom_font).grid(row=1, column=0, padx=10, pady=5)
        self.name_entry_edit = tk.Entry(self.edit_window, font=self.custom_font)
        self.name_entry_edit.insert(0, item[1])
        self.name_entry_edit.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.edit_window, text="Quantity", font=self.custom_font).grid(row=2, column=0, padx=10, pady=5)
        self.quantity_entry_edit = tk.Entry(self.edit_window, font=self.custom_font)
        self.quantity_entry_edit.insert(0, item[2])
        self.quantity_entry_edit.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.edit_window, text="Price", font=self.custom_font).grid(row=3, column=0, padx=10, pady=5)
        self.price_entry_edit = tk.Entry(self.edit_window, font=self.custom_font)
        self.price_entry_edit.insert(0, item[3])
        self.price_entry_edit.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.edit_window, text="Details", font=self.custom_font).grid(row=4, column=0, padx=10, pady=5)
        self.details_entry_edit = tk.Entry(self.edit_window, font=self.custom_font)
        self.details_entry_edit.insert(0, item[4])
        self.details_entry_edit.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.edit_window, text="Save", font=self.custom_font, command=lambda: self.save_item(index)).grid(row=5, column=0, columnspan=2, pady=10)

    def save_item(self, index):
        serial = self.serial_entry_edit.get()
        name = self.name_entry_edit.get()
        quantity = self.quantity_entry_edit.get()
        price = self.price_entry_edit.get()
        details = self.details_entry_edit.get()

        if serial and name and quantity and price and details:
            self.inventory[index] = (serial, name, int(quantity), float(price), details)
            self.edit_window.destroy()
            self.refresh_product_list()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields")

    def delete_item(self, index):
        del self.inventory[index]
        self.refresh_product_list()

if __name__ == "__main__":
    root = tk.Tk()
    desired_width = 1150
    desired_height = 500
    root.geometry(f"{desired_width}x{desired_height}")
    
    root.iconbitmap('InventoriaIcon.ico')
    
    app = InventorySystem(root)
    
    notice_label = tk.Label(root, text="© 2024 RazzCodes. All Rights Reserved.", font=("Century Gothic", 10), fg="gray")
    notice_label.grid(row=10, column=0, columnspan=5, sticky='se', padx=30, pady=(0,30))
    
    root.mainloop()
