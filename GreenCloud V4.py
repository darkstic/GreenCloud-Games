import sys
import ast
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


categories = {
    "Driving": [["Slow Roads", "https://slowroads.io/"]],
    "Shooter": [["Deadshot FPS", "https://deadshot.io/"], ["Knockoff Fortnite", "https://1v1.lol/"]],
    "Horror": [["Slide in The Woods", "https://horrorgames.io/slide-in-the-woods"]],
    "Exploration": [["Geogussr Free", "https://openguessr.com/"]],
    "Puzzle": [["what beats rock?", "https://www.whatbeatsrock.com/"]],
    "Easy-to-run": [["Best Paper.io", "https://paper-io.com/conflict/"]],
    "Custom": [],
}

# Load custom categories from file
def load_custom_category():
    if os.path.isfile("custom.txt"):
        with open("custom.txt", "r") as file:
            custom_items = ast.literal_eval(file.read())
            categories["Custom"] = custom_items

# Save custom category to file
def save_custom_category():
    with open("custom.txt", "w") as file:
        file.write(str(categories["Custom"]))

# PyQt Browser Class
class BrowserApp(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("GreenCLoud Game Window")
        self.setGeometry(100, 100, 800, 600)

        # Create a layout and embedded browser
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        # Load the selected URL
        self.browser.setUrl(QUrl(url))

# Tkinter Interface
class URLManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Menu")
        self.root.geometry("400x400")

        # Category dropdown
        self.category_label = tk.Label(self.root, text="Select Category:")
        self.category_label.pack(pady=5)
        self.category_var = tk.StringVar(value=list(categories.keys())[0])
        self.category_dropdown = ttk.Combobox(self.root, textvariable=self.category_var, values=list(categories.keys()))
        self.category_dropdown.pack(pady=5)

        # Items list
        self.items_label = tk.Label(self.root, text="Select an Item:")
        self.items_label.pack(pady=5)
        self.items_listbox = tk.Listbox(self.root, height=10)
        self.items_listbox.pack(pady=5, fill=tk.BOTH, expand=True)
        self.update_items()

        # Buttons
        self.open_button = tk.Button(self.root, text="Launch Selected Game", command=self.open_in_browser)
        self.open_button.pack(pady=5)
        self.add_button = tk.Button(self.root, text="Add Custom URL", command=self.add_custom_url)
        self.add_button.pack(pady=5)

        # Event bindings
        self.category_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_items())

    def update_items(self):
        category = self.category_var.get()
        self.items_listbox.delete(0, tk.END)
        for item in categories[category]:
            self.items_listbox.insert(tk.END, item[0])

    def open_in_browser(self):
        category = self.category_var.get()
        selected_index = self.items_listbox.curselection()
        if selected_index:
            item_index = selected_index[0]
            url = categories[category][item_index][1]

            # Launch the PyQt browser with the selected URL
            app = QApplication(sys.argv)
            browser = BrowserApp(url)
            browser.show()
            app.exec_()
        else:
            messagebox.showerror("Error", "No item selected!")

    def add_custom_url(self):
        name = simpledialog.askstring("Custom URL", "Enter the name of the URL:")
        if not name:
            return
        url = simpledialog.askstring("Custom URL", "Enter the URL:")
        if not url:
            return
        categories["Custom"].append([name, url])
        save_custom_category()
        if self.category_var.get() == "Custom":
            self.update_items()

    def run(self):
        self.root.mainloop()

# Main Function
if __name__ == "__main__":
    load_custom_category()
    url_manager = URLManagerApp()
    url_manager.run()
