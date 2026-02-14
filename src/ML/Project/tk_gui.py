import tkinter as tk
import numpy as np


class SalaryPredictorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Salary Predictor")
        self.master.geometry("300x200")

        self.label = tk.Label(master, text="Enter years of experience:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.predict_button = tk.Button(master, text="Predict Salary", command=self.predict_salary)
        self.predict_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def create_Widget(self):
        header_label = tk.Label(self.master, text="Salary Predictor App",bg="lightblue", fg="white" , font=("Arial", 20, "bold"))
        header_label.pack(fill=tk.X)  # Make the header label span the entire width of the window
        header_label.pack(pady=10)

    def predict_salary(self):
        try:
            years_experience = float(self.entry.get())
            # Dummy prediction logic (replace with actual model prediction)
            predicted_salary = 5000 + (years_experience * 1000)  # Example formula
            self.result_label.config(text=f"Predicted Salary: ${predicted_salary:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number for years of experience.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredictorApp(root)
    root.mainloop()