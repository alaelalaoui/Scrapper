import tkinter as tk

def show_answer():
    question = entry.get()
    if question.strip():
        answer_label.config(text=f"Answer to '{question}': [Your answer here]")
    else:
        answer_label.config(text="Please enter a question.")

# Create the main window
root = tk.Tk()
root.title("Question and Answer App")

# Create and place the Entry widget for question input
entry_label = tk.Label(root, text="Enter your question:")
entry_label.pack(pady=(10, 0))
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create and place the Button widget
button = tk.Button(root, text="Get Answer", command=show_answer)
button.pack(pady=10)

# Create and place the Label widget for displaying the answer
answer_label = tk.Label(root, text="", wraplength=400)
answer_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
