import tkinter as tk
from tkinter import ttk
import subprocess

def get_selected_birthdate():
    selected_year = year_combobox.get()
    selected_month = month_combobox.get()
    selected_day = day_combobox.get()
    
    # Combine the selected values into YYYY-MM-DD format
    selected_birthdate = f"{selected_year}-{selected_month}-{selected_day}"
    
    # Close the tkinter window
    root.destroy()
    
    # Run the life_progress_bar.py script with the selected birthdate as an argument
    subprocess.run(["python", "life_progress_bar.py", selected_birthdate])



def get_selected_birthdate():
    selected_year = year_combobox.get()
    selected_month = month_combobox.get()
    selected_day = day_combobox.get()
    
    # Combine the selected values into YYYY-MM-DD format
    selected_birthdate = f"{selected_year}-{selected_month}-{selected_day}"
    
    root.destroy()  # Close the tkinter window
    return selected_birthdate

root = tk.Tk()
root.title("Select Birthdate")

# Create dropdown menus for year, month, and day
years = [str(year) for year in range(2023, 1900, -1)]  # Range of years
months = [str(month).zfill(2) for month in range(1, 13)]  # Add leading zeros to months
days = [str(day).zfill(2) for day in range(1, 32)]  # Add leading zeros to days

year_label = tk.Label(root, text="Year:", font=("Arial", 12))
year_label.grid(row=0, column=0)
year_combobox = ttk.Combobox(root, values=years)
year_combobox.grid(row=0, column=1)

month_label = tk.Label(root, text="Month:", font=("Arial", 12))
month_label.grid(row=0, column=2)
month_combobox = ttk.Combobox(root, values=months)
month_combobox.grid(row=0, column=3)

day_label = tk.Label(root, text="Day:", font=("Arial", 12))
day_label.grid(row=0, column=4)
day_combobox = ttk.Combobox(root, values=days)
day_combobox.grid(row=0, column=5)

submit_button = tk.Button(root, text="Submit", command=get_selected_birthdate)
submit_button.grid(row=1, column=0, columnspan=6)

# Set the size of the window
window_width = 600  # Adjust the width as needed
window_height = 100  # Adjust the height as needed
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
