import math
import cmath
import tkinter as tk
from tkinter import messagebox, scrolledtext

variables = {}

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return cmath.sqrt(x) 
    else:
        return math.sqrt(x)
        
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number."
    elif x == 0:
        return 1
    else:
        return math.factorial(x)

def evaluate_expression(expression):
    try:
        result = eval(expression, {
            'sin': sine,
            'cos': cosine,
            'tan': tangent,
            'sqrt': sqrt,
            'factorial': factorial,
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
            '**': exponentiate,
            **variables  
        })
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."
    except ValueError:
        return "Error! Invalid input expression."
    except Exception as e:
        return f"Error! {str(e)}"

def calculator():
    
    root = tk.Tk()
    root.title("Voided Calculator")

    def evaluate():
        expression = entry.get("1.0", tk.END).strip() 
        result = evaluate_expression(expression)
        result_label.config(text=f"Result: {result}")
        history_text.insert(tk.END, f"{expression} = {result}\n")
        history_text.see(tk.END) 

    def assign():
        var_name = var_name_entry.get()
        var_value = var_value_entry.get()
        message = assign_variable(var_name, var_value)
        messagebox.showinfo("Variable Assignment", message)

    def clear_history():
        history_text.delete("1.0", tk.END)

    entry_label = tk.Label(root, text="Enter expression:")
    entry = tk.Text(root, height=3, width=50)
    evaluate_button = tk.Button(root, text="Evaluate", command=evaluate)
    result_label = tk.Label(root, text="Result: ")

    var_name_label = tk.Label(root, text="Variable Name:")
    var_value_label = tk.Label(root, text="Variable Value:")
    var_name_entry = tk.Entry(root, width=20)
    var_value_entry = tk.Entry(root, width=20)
    assign_button = tk.Button(root, text="Assign Variable", command=assign)

    history_label = tk.Label(root, text="History:")
    history_text = tk.scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
    clear_history_button = tk.Button(root, text="Clear History", command=clear_history)

    entry_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
    evaluate_button.grid(row=0, column=3, padx=10, pady=10)
    result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W)

    var_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    var_value_label.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
    var_name_entry.grid(row=3, column=0, padx=10, pady=10)
    var_value_entry.grid(row=3, column=1, padx=10, pady=10)
    assign_button.grid(row=3, column=2, padx=10, pady=10)

    history_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    history_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
    clear_history_button.grid(row=6, column=0, padx=10, pady=10)

    root.mainloop()

calculator()
