import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Function to parse the equation and calculate Gaussian error propagation
def calculate_error():
    try:
        equation = entry_equation.get()  # Get equation from input
        variables = list(sp.symbols(entry_variables.get()))  # Parse variables
        eq = sp.sympify(equation)  # Convert string to symbolic equation
        
        # Get the error for each variable
        error_values = list(map(float, entry_errors.get().split(',')))
        
        if len(variables) != len(error_values):
            raise ValueError("Number of variables and errors should be the same.")
        
        # Optional: Get the values for each variable (if provided)
        values_input = entry_values.get().strip()
        if values_input:
            variable_values = list(map(float, values_input.split(',')))
            if len(variable_values) != len(variables):
                raise ValueError("Number of variables and values should be the same.")
        else:
            variable_values = None
        
        # Calculate the partial derivatives of the equation w.r.t. each variable
        partial_derivatives = [sp.diff(eq, var) for var in variables]
        
        # Gaussian error propagation formula (symbolic)
        squared_errors = sum((partial_derivatives[i] ** 2) * (error_values[i] ** 2) for i in range(len(variables)))
        total_error_symbolic = sp.sqrt(squared_errors)
        
        result = f"Gaussian Error (Symbolic): {total_error_symbolic}"
        
        # If values are provided, calculate the actual numeric error
        if variable_values is not None:
            substitutions = {variables[i]: variable_values[i] for i in range(len(variables))}
            total_error_numeric = total_error_symbolic.evalf(subs=substitutions)
            
            # Calculate the actual value of the equation
            equation_value = eq.evalf(subs=substitutions)
            
            # Calculate the relative error
            relative_error = total_error_numeric / abs(equation_value) if equation_value != 0 else float('inf')
            
            result += f"\nActual Error: {total_error_numeric}"
            result += f"\nEquation Value: {equation_value}"
            result += f"\nRelative Error: {relative_error * 100:.2f}%"
        
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)  # Clear previous result
            result_text.insert(tk.END, result)  # Insert new result
            result_text.config(state=tk.DISABLED)  # Make it read-only again
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Gaussian Error Propagation Calculator")

# Create input fields and labels
label_equation = tk.Label(root, text="Equation:")
label_equation.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="e")
entry_equation = tk.Entry(root, width=50)
entry_equation.grid(row=0, column=1, padx=(0, 20), pady=(20, 10), sticky="ew")

label_variables = tk.Label(root, text="Variables (comma separated):")
label_variables.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="e")
entry_variables = tk.Entry(root, width=50)
entry_variables.grid(row=1, column=1, padx=(0, 20), pady=10, sticky="ew")

label_errors = tk.Label(root, text="Errors for variables (comma separated):")
label_errors.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="e")
entry_errors = tk.Entry(root, width=50)
entry_errors.grid(row=2, column=1, padx=(0, 20), pady=10, sticky="ew")

label_values = tk.Label(root, text="Values of variables (optional, comma separated):")
label_values.grid(row=3, column=0, padx=(20, 10), pady=(10, 20), sticky="e")
entry_values = tk.Entry(root, width=50)
entry_values.grid(row=3, column=1, padx=(0, 20), pady=(10, 20), sticky="ew")

# Create a button to calculate the error
button_calculate = tk.Button(root, text="Calculate Error", command=calculate_error)
button_calculate.grid(row=4, column=0, columnspan=2, pady=20)

# Change button color and style
button_calculate.config(
    bg="#4CAF50",  # A modern green color
    fg="white",
    font=("Roboto", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.FLAT,
    borderwidth=0,
    activebackground="#45a049"  # Slightly darker green for when button is pressed
)

# Add hover effect
def on_enter(e):
    button_calculate['background'] = '#45a049'

def on_leave(e):
    button_calculate['background'] = '#4CAF50'

button_calculate.bind("<Enter>", on_enter)
button_calculate.bind("<Leave>", on_leave)

# Create a label to display the result
result_text = tk.Text(root)
result_text.grid(row=5, column=0, columnspan=2)

# make it look nicer
font_label = ("Roboto", 14, "bold")
font_entry = ("Roboto", 14)
font_result = ("Consolas", 12)

# Apply to labels
label_equation.config(font=font_label)
label_variables.config(font=font_label)
label_errors.config(font=font_label)
label_values.config(font=font_label)

# Apply to entries
entry_equation.config(font=font_entry)
entry_variables.config(font=font_entry)
entry_errors.config(font=font_entry)
entry_values.config(font=font_entry)

# Apply to result text
result_text.config(font=font_result)

# change scrollbar and textbox
result_text.config(bg="lightgray", fg="black", font=font_result)
scrollbar = tk.Scrollbar(root, command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=2, sticky='nsew')


# Run the main event loop
root.mainloop()
