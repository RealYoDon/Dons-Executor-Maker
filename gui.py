import tkinter as tk
from tkinter import scrolledtext

def execute_script():
    script_content = script_input.get("1.0", tk.END)  # Get text from input
    print("Executing script:\n", script_content)  # Placeholder for execution logic

# Create the main window
root = tk.Tk()
root.title("Dons Executor")
root.geometry("400x300")  # Set window size

# Label for input
label = tk.Label(root, text="Insert Scripts:", font=("Arial", 12))
label.pack(pady=5)

# Text input box
script_input = scrolledtext.ScrolledText(root, width=50, height=10)
script_input.pack(pady=5)

# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_script, font=("Arial", 12))
execute_button.pack(pady=10)

# Run the GUI
root.mainloop()
