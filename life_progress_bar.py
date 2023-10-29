import datetime
import tkinter as tk

# Function to update the progress bars
def update_progress_bars():
    current_datetime = datetime.datetime.now()
    time_elapsed = current_datetime - birthdate_datetime
    total_seconds_in_life = (target_datetime - birthdate_datetime).total_seconds()

    # Calculate the percentage of life already lived
    percentage_lived = (time_elapsed.total_seconds() / total_seconds_in_life) * 100

    # Calculate the percentage of time remaining
    percentage_remaining = 100 - percentage_lived

    # Update the progress bars
    progress_bar_canvas.coords(progress_bar_lived, 0, 0, percentage_lived * canvas_width / 100, canvas_height)
    progress_bar_canvas.coords(progress_bar_remaining, canvas_width, 0,
                              canvas_width - (percentage_remaining * canvas_width / 100), canvas_height)

    # Format the percentages to display exactly six decimal places
    formatted_percentage_lived = f"{percentage_lived:.8f}"
    formatted_percentage_remaining = f"{percentage_remaining:.8f}"

    # Update the labels with the formatted percentages
    percentage_label_lived.config(text=f"Percentage of Life Lived: {formatted_percentage_lived}%")
    percentage_label_remaining.config(text=f"Percentage Remaining: {formatted_percentage_remaining}%")

    # Call this function again after 1000 milliseconds (1 second)
    root.after(1000, update_progress_bars)

# Create the main window
root = tk.Tk()
root.title("Life Progress Bars")

# Enter your birthdate in the format: YYYY-MM-DD
birthdate_str = 'your birthdate'
birthdate_datetime = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
target_year = birthdate_datetime.year + 76
target_datetime = datetime.datetime(target_year, birthdate_datetime.month, birthdate_datetime.day, 0, 0, 0)

# Create labels to display the percentages
percentage_label_lived = tk.Label(root, text="", font=("Arial", 12))
percentage_label_lived.pack()
percentage_label_remaining = tk.Label(root, text="", font=("Arial", 12))
percentage_label_remaining.pack()

# Create a canvas for the progress bars
canvas_width = 300
canvas_height = 20
progress_bar_canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="light gray")
progress_bar_canvas.pack()

# Create the progress bars (lived in green and remaining in red)
progress_bar_lived = progress_bar_canvas.create_rectangle(0, 0, 0, canvas_height, fill="green")
progress_bar_remaining = progress_bar_canvas.create_rectangle(canvas_width, 0, canvas_width, canvas_height, fill="red")

# Start updating the progress bars
update_progress_bars()

# Run the main loop
root.mainloop()
