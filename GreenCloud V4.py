import sys
import ast
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

version = "4.4.5"

listy_type = "stable"

categories_extended = {
    "Driving": [
        ["Slow Roads", "https://slowroads.io/"],
    ],
    "Shooter": [
        ["Knockoff Fortnite", "https://1v1.lol/"],
    ],
    "Horror": [
        ["Slide in The Woods (Playable at highest sensitivity)", "https://horrorgames.io/slide-in-the-woods"]
    ],
    "Exploration": [
        ["Geogussr Free", "https://openguessr.com/"],
    ],
    "Puzzle": [
        ["what beats rock?", "https://www.whatbeatsrock.com/"]
    ],
    "Easy-to-run": [
        ["Best Paper.io", "https://paper-io.com/conflict/"]
    ],
    "Custom": [],
}

categories_basic = {
    "Stable": [
        ["Slow Roads (Original)", "https://old.slowroads.io/"],
        ["Knockoff Fortnite", "https://1v1.lol/"],
        ["Best Paper.io", "https://paper-io.com/conflict/"],
        ["Slide in The Woods (Playable at highest sensitivity)", "https://horrorgames.io/slide-in-the-woods"],
        ["What beats rock?", "https://www.whatbeatsrock.com/"],
        ["Body Cam Shooter", "https://www.silvergames.com/en/bodycamera-shooter"],
        ["Agar", "https://agar.io/"],
        ["Geometry Dash", "https://geometrygame.org/"],
        ["Funny Blade & Magic","https://www.silvergames.com/en/funny-blade-and-magic"],
        ["Crossy Road","https://crossy-road.com/"],
        ["Polytrack","https://polytrack.org/"],

    ]
}

Testing_phase = {
    "Testing": [
        ["SLow Roads (Graphics +)","https://slowroads.io/"],
        ["Getaway Shootout","getawayshootout.com"],
        ["Granny","https://www.granny-online.com/g/granny-2-chapter-2"],
        ["ShellShockers","https://shellshock.io/"],
                


    ]
}

if listy_type == "stable":
    categories = categories_basic
elif listy_type == "extended":
    categories = categories_extended
elif listy_type == "testing":
    categories = Testing_phase


def save_custom_category():
    with open("C:\\Users\\Public\\Documents\\custom.txt", "w") as file:
        file.write(str(categories["Custom"]))


# PyQt Browser Class
class BrowserApp(QMainWindow):
    def __init__(self, url, enable_hardware_acceleration):
        super().__init__()
        self.setWindowTitle("GreenCLoud Game Window")

        # Get the screen geometry of the primary display
        screen_geometry = QDesktopWidget().screenGeometry()
        self.resize(screen_geometry.width(), screen_geometry.height())
        self.move(0, 0)

        # Create a layout and embedded browser
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        # Enable or disable hardware acceleration based on the checkbox state
        if enable_hardware_acceleration:
            self.browser.settings().setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
            self.browser.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)

        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        # Debugging output
        print(f"Opening URL: {url}")


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

        # Hardware acceleration checkbox
        self.hw_accel_var = tk.BooleanVar()
        self.hw_accel_checkbox = tk.Checkbutton(self.root, text="Enable Hardware Acceleration", variable=self.hw_accel_var)
        self.hw_accel_checkbox.pack(pady=5)

        # Launch button
        self.open_button = tk.Button(self.root, text="Launch Selected Game", command=self.open_in_browser)
        self.open_button.pack(pady=5)

    def update_items(self):
        self.items_listbox.delete(0, tk.END)
        category = self.category_var.get()
        for item in categories[category]:
            self.items_listbox.insert(tk.END, item[0])

    def open_in_browser(self):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            selected_item = self.items_listbox.get(selected_index)
            category = self.category_var.get()
            url = next(item[1] for item in categories[category] if item[0] == selected_item)
            self.launch_browser(url)

    def launch_browser(self, url):
        enable_hardware_acceleration = self.hw_accel_var.get()
        app = QApplication(sys.argv)
        browser_app = BrowserApp(url, enable_hardware_acceleration)
        browser_app.show()
        sys.exit(app.exec_())

# Example usage
if __name__ == "__main__":
    url_manager_app = URLManagerApp()
    url_manager_app.root.mainloop()
