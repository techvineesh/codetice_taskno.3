import difflib
import tkinter as tk
from tkinter import scrolledtext

# Function to calculate text similarity using difflib
def calculate_similarity(text1, text2):
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
    return similarity

# Function to check for plagiarism
def check_for_plagiarism():
    input_text = input_text_widget.get("1.0", "end-1c")  # Get input text
    reference_text = reference_text_widget.get("1.0", "end-1c")  # Get reference text

    similarity = calculate_similarity(input_text, reference_text)

    if similarity >= 0.8:
        result_text_widget.configure(state='normal')
        result_text_widget.delete(1.0, 'end')
        result_text_widget.insert(tk.END, f"Plagiarism detected! Similarity: {similarity}")
        result_text_widget.configure(state='disabled')
    else:
        result_text_widget.configure(state='normal')
        result_text_widget.delete(1.0, 'end')
        result_text_widget.insert(tk.END, f" plagiarism detected. Similarity: {similarity}")
        result_text_widget.configure(state='disabled')

# Create the main window
window = tk.Tk()
window.title("Plagiarism Checker")

# Create and configure input text widget
input_text_widget = scrolledtext.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
input_text_widget.grid(row=0, column=0, padx=10, pady=10)
input_text_widget.insert(tk.END, "Enter your text here...")

# Create and configure reference text widget
reference_text_widget = scrolledtext.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
reference_text_widget.grid(row=1, column=0, padx=10, pady=10)
reference_text_widget.insert(tk.END, "Enter the reference text here...")

# Create and configure result text widget
result_text_widget = scrolledtext.ScrolledText(window, width=50, height=3, wrap=tk.WORD)
result_text_widget.grid(row=2, column=0, padx=10, pady=10)
result_text_widget.insert(tk.END, "Plagiarism result will be displayed here...")
result_text_widget.configure(state='disabled')

# Create and configure the "Check Plagiarism" button
check_button = tk.Button(window, text="Check Plagiarism", command=check_for_plagiarism)
check_button.grid(row=3, column=0, pady=10)

window.mainloop()
