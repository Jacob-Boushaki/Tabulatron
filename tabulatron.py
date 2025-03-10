import tkinter as tk
from tkinter import messagebox, ttk
import csv

GOLDEN_RATIO = 1.61803398875
TITLEBAR_HEIGHT = 31
BG_COLOR = "#C7C7F3"

class Tabulatron:
    def __init__(self, master):
        # Some basic setup
        self.master = master
        self.master.option_add("*Font", "Cambria")

        # Dictionary definitions
        self.criteria_names = {
            1: "Invention",
            2: "Marketability",
            3: "Presentation",
            4: "Ambition",
            5: "Creation",
            6: "Technology"
        }
        self.bonus_criteria = {
            1: "Sustainability",
            2: "T",
            3: "Accessibility",
            4: "Representation",
        }

        # Window graphics dimensions
        window_height = 550
        window_width = int((window_height + TITLEBAR_HEIGHT) * GOLDEN_RATIO)

        # Window Settings
        self.master.title("Tabulatron")
        self.master.geometry(f"{window_width}x{window_height}")
        self.master.configure(bg=BG_COLOR)

        # judge label and input field
        self.judge_test = tk.Label(master, text="Judge number:", bg=BG_COLOR)
        self.judge_test.pack(side="top", expand=False, fill="y")
        self.entry_judge = tk.Entry(master)
        self.entry_judge.pack(side="top", expand=False)

        # frame for criteria entries
        self.criteria_frame = tk.Frame(master, bg=BG_COLOR)
        self.criteria_frame.pack(pady=10)

        self.criteria_entries = []

        # Create labels and entry fields for 5 projects side by side
        for project in range(5):
            project_label = tk.Label(self.criteria_frame, text=f"Project {project + 1}", bg=BG_COLOR, font=("Cambria", 10, "bold"))
            project_label.grid(row=0, column=project * 2, columnspan=2, pady=(10, 0))

            for i in range(len(self.criteria_names)):
                label = tk.Label(self.criteria_frame, text=f"{self.criteria_names[i+1]}:", bg=BG_COLOR)
                label.grid(row=i + 1, column=project * 2, padx=5, pady=5)
                entry = tk.Entry(self.criteria_frame, width=10)
                entry.grid(row=i + 1, column=project * 2 + 1, padx=5, pady=5)
                self.criteria_entries.append((project, i, entry))

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.print_fields)
        self.submit_button.pack(side="top", expand=False, padx=10, pady=10)

    def print_fields(self):
        print(f"Judge number: {self.entry_judge.get()}")
        for project, i, entry in self.criteria_entries:
            print(f"Project {project + 1}, {self.criteria_names[i + 1]}: {entry.get()}")

# Create the main window and run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = Tabulatron(root)
    root.mainloop()

"""
    Future features
    when you press enter it goes to the next entry
    Submission boxes will be smaller, and only accept integers
    All fields will fit onto the same screen 
    
"""