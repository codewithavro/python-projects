import tkinter as tk

import colors

from addition import Addition

from subtraction import Subtraction

from multiplication import Multiplication

from division import Division

from floor_division import FloorDivision

from operator_function import OperatorFunctions

class Calculator:

    def __init__(self,root):

        self.root = root

        # Window

        self.root.title("CalcForge")
        self.root.geometry("420x600")
        self.root.resizable(False, False)
        self.root.configure(bg=colors.BACKGROUND)

        # Operation objects
        self.addition = Addition()
        self.subtraction = Subtraction()
        self.multiplication = Multiplication()
        self.division = Division()
        self.floor_division = FloorDivision()
        self.operator_functions = OperatorFunctions()

        # Calculator data
        self.first_number = None
        self.operation = None

        # Create GUI
        self.create_display()
        self.create_buttons()

    # -------------------------------
    # DISPLAY
    # -------------------------------

    def create_display(self):

        self.display = tk.Entry(
            self.root,
            font=("Arial", 28),
            justify="right",
            bg=colors.DISPLAY_BG,
            fg=colors.DISPLAY_FG,
            insertbackground=colors.DISPLAY_FG,
            relief="flat"
        )

        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=20,
            ipady=15,
            sticky="nsew"
        )

    # -------------------------------
    # BUTTONS
    # -------------------------------

    def create_buttons(self):

        buttons = [
            ("7", 1, 0),

            ("8", 1, 1),

            ("9", 1, 2),

            ("/", 1, 3),

            ("4", 2, 0),

            ("5", 2, 1),
            
            ("6", 2, 2),
            ("*", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),

            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("//", 4, 3),

            ("%", 5, 0),
            ("**", 5, 1),
            ("+/-", 5, 2),
            ("=", 5, 3),

            ("C", 6, 0),
            ("NEG", 6, 1),
            ("POS", 6, 2),
            ("MOD", 6, 3)
        ]

        for text, row, column in buttons:

            if text.isdigit() or text == ".":

                background = colors.NUMBER_BUTTON

            elif text == "=":

                background = colors.EQUAL_BUTTON

            elif text == "C":

                background = colors.CLEAR_BUTTON

            else:

                background = colors.OPERATOR_BUTTON

            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 16, "bold"),
                bg=background,
                fg=colors.TEXT_COLOR,
                activebackground=background,
                activeforeground=colors.TEXT_COLOR,
                relief="flat",
                command=lambda value=text:
                    self.button_click(value)
            )

            button.grid(
                row=row,
                column=column,
                padx=5,
                pady=5,
                ipadx=10,
                ipady=15,
                sticky="nsew"
            )

        # Grid configuration

        for row in range(7):
            self.root.grid_rowconfigure(
                row,
                weight=1
            )

        for column in range(4):
            self.root.grid_columnconfigure(
                column,
                weight=1
            )

    # -------------------------------
    # BUTTON CLICK
    # -------------------------------

    def button_click(self, value):

        if value.isdigit() or value == ".":

            self.display.insert(
                tk.END,
                value
            )

        elif value == "C":

            self.clear()

        elif value == "=":

            self.calculate()

        elif value == "+/-":

            self.change_sign()

        elif value == "NEG":

            self.unary_operation("negative")

        elif value == "POS":

            self.unary_operation("positive")

        else:

            self.set_operation(value)

    # -------------------------------
    # SET OPERATION
    # -------------------------------

    def set_operation(self, operation):

        try:

            self.first_number = float(
                self.display.get()
            )

            self.operation = operation

            self.display.delete(
                0,
                tk.END
            )

        except ValueError:

            self.show_error("Invalid")

    # -------------------------------
    # CALCULATE
    # -------------------------------

    def calculate(self):

        try:

            second_number = float(
                self.display.get()
            )

            result = self.perform_operation(
                self.first_number,
                second_number,
                self.operation
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                self.format_result(result)
            )

            self.first_number = result
            self.operation = None

        except ZeroDivisionError:

            self.show_error(
                "Cannot divide by 0"
            )

        except Exception:

            self.show_error("Error")

    # -------------------------------
    # PERFORM OPERATION
    # -------------------------------

    def perform_operation(
        self,
        a,
        b,
        operation
    ):

        if operation == "+":

            return self.addition.calculate(
                a,
                b
            )

        elif operation == "-":

            return self.subtraction.calculate(
                a,
                b
            )

        elif operation == "*":

            return self.multiplication.calculate(
                a,
                b
            )

        elif operation == "/":

            return self.division.calculate(
                a,
                b
            )

        elif operation == "//":

            return self.floor_division.calculate(
                a,
                b
            )

        elif operation == "%":

            return self.operator_functions.modulo(
                a,
                b
            )

        elif operation == "**":

            return self.operator_functions.power(
                a,
                b
            )

        else:

            raise ValueError(
                "Unknown operation"
            )

    # -------------------------------
    # SIGN
    # -------------------------------

    def change_sign(self):

        try:

            number = float(
                self.display.get()
            )

            result = self.operator_functions.negative(
                number
            )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                self.format_result(result)
            )

        except ValueError:

            self.show_error("Invalid")

    # -------------------------------
    # UNARY OPERATION
    # -------------------------------

    def unary_operation(self, operation):

        try:

            number = float(
                self.display.get()
            )

            if operation == "negative":

                result = self.operator_functions.negative(
                    number
                )

            elif operation == "positive":

                result = self.operator_functions.positive(
                    number
                )

            else:

                raise ValueError(
                    "Invalid operation"
                )

            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                self.format_result(result)
            )

        except ValueError:

            self.show_error("Invalid")

    # -------------------------------
    # CLEAR
    # -------------------------------

    def clear(self):

        self.display.delete(
            0,
            tk.END
        )

        self.first_number = None
        self.operation = None

    # -------------------------------
    # ERROR
    # -------------------------------

    def show_error(self, message):

        self.display.delete(
            0,
            tk.END
        )

        self.display.insert(
            0,
            message
        )

    # -------------------------------
    # FORMAT RESULT
    # -------------------------------

    def format_result(self, result):

        if (
            isinstance(result, float)
            and result.is_integer()
        ):

            return str(int(result))

        return str(result)


# ===================================
# PROGRAM START
# ===================================

if __name__ == "__main__":

    root = tk.Tk()

    calculator = Calculator(root)

    root.mainloop()