# Inventory System using Tkinter

This is a simple inventory management system implemented using Tkinter in Python. It allows users to add, delete, edit, and search for items in an inventory.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Features](#features)
4. [Usage](#usage)
5. [License](#license)
6. [Code Structure](#code-structure)

## Introduction <a name="introduction"></a>

This inventory system provides a graphical user interface (GUI) for managing inventory items. It's designed using Tkinter, which is a standard GUI toolkit for Python.

## Setup <a name="setup"></a>

To run the application, you need Python installed on your system. Additionally, you need to install the Pillow library for image processing. You can install it using pip:

```bash
pip install Pillow
```

Once installed, you can run the `main.py` file to start the application.

## Features <a name="features"></a>

- **Add Items**: Users can add new items to the inventory by providing details such as serial number, name, quantity, price, and details.
- **Delete Items**: Items can be removed from the inventory either individually or in bulk.
- **Edit Items**: Users can edit the details of existing items.
- **Search Functionality**: Items in the inventory can be searched based on their serial number or name.
- **GUI with Background Image**: The application has a visually appealing GUI with a background image.

## Usage <a name="usage"></a>

1. **Adding Items**: Click on the "Add +" button to open a new window where you can input details of the item to be added.
2. **Deleting Items**: Select the items you want to delete by checking the checkboxes next to them and then click on the "Delete -" button.
3. **Editing Items**: Click on the "Update" button next to the item you want to edit, which opens a window where you can modify the item's details.
4. **Searching Items**: Enter a query in the search bar to filter items based on their serial number or name.

## License <a name="license"></a>

© 2024 RazzCodes. All Rights Reserved.

## Code Structure <a name="code-structure"></a>

### Importing Libraries

```python
import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk  
```

### InventorySystem Class

```python
class InventorySystem:
    def __init__(self, root):
        # Initialization code...
```

### Initializing GUI and Background Image

```python
self.background_image = Image.open("Forest.jpg")
# More initialization code...
```

### Creating UI Components

```python
def create_widgets(self):
    # UI components creation code...
```

### Scrolling Text

```python
def scroll_text(self):
    # Text scrolling animation code...
```

### Searching Items

```python
def search_item(self, event):
    # Search functionality code...
```

### Adding Item Form

```python
def add_item_form(self):
    # Form for adding items code...
```

### Adding Item

```python
def add_item(self):
    # Adding item to inventory code...
```

### Removing Item

```python
def remove_item(self):
    # Removing item from inventory code...
```
### Refreshing Product List

```python
def refresh_product_list(self, query=""):
    # Refreshing product list code...
```

### Editing Item

```python
def edit_item(self, index):
    # Editing item details code...
```
### Saving Edited Item

```python
def save_item(self, index):
    # Saving edited item details code...
```
### Deleting Item

```python
def delete_item(self, index):
    # Deleting item from inventory code...
```
### Main Function

```python
if __name__ == "__main__":
    # Main function code...
```
