import tkinter.messagebox

from Matrix import Matrix, OperateMatrix
import tkinter as tk

window = tk.Tk()
window.title("Matrix Calculator")
window.geometry("600x400")
window.iconphoto(False, tk.PhotoImage(file="icons/app_icon.png"))

matrix1 = Matrix()
matrix2 = Matrix()
operation = OperateMatrix()


def fill_sample1_m1():
    input1.insert(0, "1,2,3,4,5,6,7,8,9")


def fill_sample1_m2():
    input2.insert(0, "1,2,3,4,5,6,7,8,9")


def construct_matrices():
    try:
        global matrix1, matrix2, operation

        matri1 = Matrix()
        matri1.construct_matrix(input1.get())
        matri2 = Matrix()
        matri2.construct_matrix(input2.get())
        matrix1 = matri1
        matrix2 = matri2


        operation = OperateMatrix(matrix1, matrix2)
        show_matrix1.config(text=f"Your Matrix1:\n{matrix1}")
        show_matrix2.config(text=f"Your Matrix1:\n{matrix2}")

    except ValueError:
        tkinter.messagebox.showerror("Value Error", "Please Enter a Valid Input or Construct")
        input1.delete(0, "end")
        input2.delete(0, "end")


def add():
    try:
        result.config(text=operation.add_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input or Construct")
        input1.delete(0, "end")
        input2.delete(0, "end")


def sub():
    try:
        result.config(text=operation.sub_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input or Construct")
        input1.delete(0, "end")
        input2.delete(0, "end")


def mul():
    try:
        result.config(text=operation.mul_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input or Construct")
        input1.delete(0, "end")
        input2.delete(0, "end")


def show_dets():
    try:
        result.config(text=f"Determinant of first matrix is {matrix1.determinant()}\nDeterminant of second matrix is "
                           f"{matrix2.determinant()}")

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input")
        input1.delete(0, "end")
        input2.delete(0, "end")


def show_input_window1():
    input_window = tk.Toplevel()

    def append_number(number):
        current_text = input_label_var.get()
        new_text = current_text + str(number)
        input_label_var.set(new_text)

    def send_matrix():
        input = [number+"," for number in input_label_var.get()]
        to_send = ""
        for number in input:
            to_send = to_send + number

        to_send = to_send[:-1]
        input1.insert(0, to_send)
        input_window.destroy()

    input_label_var = tk.StringVar()
    input_label_var.set("")

    matrix_display = tk.Label(input_window, textvariable=input_label_var)

    # Making Buttons
    b1 = tk.Button(input_window, text="1", width=10, height=5, command=lambda: append_number(1))
    b2 = tk.Button(input_window, text="2", width=10, height=5, command=lambda: append_number(2))
    b3 = tk.Button(input_window, text="3", width=10, height=5, command=lambda: append_number(3))
    b4 = tk.Button(input_window, text="4", width=10, height=5, command=lambda: append_number(4))
    b5 = tk.Button(input_window, text="5", width=10, height=5, command=lambda: append_number(5))
    b6 = tk.Button(input_window, text="6", width=10, height=5, command=lambda: append_number(6))
    b7 = tk.Button(input_window, text="7", width=10, height=5, command=lambda: append_number(7))
    b8 = tk.Button(input_window, text="8", width=10, height=5, command=lambda: append_number(8))
    b9 = tk.Button(input_window, text="9", width=10, height=5, command=lambda: append_number(9))
    b0 = tk.Button(input_window, text="0", width=10, height=5, command=lambda: append_number(0))
    submit_buttom = tk.Button(input_window, text="Submit", command=send_matrix)

    # Displaying Button
    b1.grid(column=0, row=0, padx=5, pady=5)
    b2.grid(column=1, row=0, padx=5, pady=5)
    b3.grid(column=2, row=0, padx=5, pady=5)
    b4.grid(column=0, row=1, padx=5, pady=5)
    b5.grid(column=1, row=1, padx=5, pady=5)
    b6.grid(column=2, row=1, padx=5, pady=5)
    b7.grid(column=0, row=2, padx=5, pady=5)
    b8.grid(column=1, row=2, padx=5, pady=5)
    b9.grid(column=2, row=2, padx=5, pady=5)
    b0.grid(column=1, row=3, padx=5, pady=5)
    submit_buttom.grid(column=0, row=5, columnspan=3)

    matrix_display.grid(column=0, row=4, columnspan=3)


def show_input_window2():
    input_window = tk.Toplevel()

    def append_number(number):
        current_text = input_label_var.get()
        new_text = current_text + str(number)
        input_label_var.set(new_text)

    def send_matrix():
        input = [number + "," for number in input_label_var.get()]
        to_send = ""
        for number in input:
            to_send = to_send + number

        to_send = to_send[:-1]
        input2.insert(0, to_send)
        input_window.destroy()

    input_label_var = tk.StringVar()
    input_label_var.set("")

    matrix_display = tk.Label(input_window, textvariable=input_label_var)

    # Making Buttons
    b1 = tk.Button(input_window, text="1", width=10, height=5, command=lambda: append_number(1))
    b2 = tk.Button(input_window, text="2", width=10, height=5, command=lambda: append_number(2))
    b3 = tk.Button(input_window, text="3", width=10, height=5, command=lambda: append_number(3))
    b4 = tk.Button(input_window, text="4", width=10, height=5, command=lambda: append_number(4))
    b5 = tk.Button(input_window, text="5", width=10, height=5, command=lambda: append_number(5))
    b6 = tk.Button(input_window, text="6", width=10, height=5, command=lambda: append_number(6))
    b7 = tk.Button(input_window, text="7", width=10, height=5, command=lambda: append_number(7))
    b8 = tk.Button(input_window, text="8", width=10, height=5, command=lambda: append_number(8))
    b9 = tk.Button(input_window, text="9", width=10, height=5, command=lambda: append_number(9))
    b0 = tk.Button(input_window, text="0", width=10, height=5, command=lambda: append_number(0))
    submit_buttom = tk.Button(input_window, text="Submit", command=send_matrix)

    # Displaying Button
    b1.grid(column=0, row=0, padx=5, pady=5)
    b2.grid(column=1, row=0, padx=5, pady=5)
    b3.grid(column=2, row=0, padx=5, pady=5)
    b4.grid(column=0, row=1, padx=5, pady=5)
    b5.grid(column=1, row=1, padx=5, pady=5)
    b6.grid(column=2, row=1, padx=5, pady=5)
    b7.grid(column=0, row=2, padx=5, pady=5)
    b8.grid(column=1, row=2, padx=5, pady=5)
    b9.grid(column=2, row=2, padx=5, pady=5)
    b0.grid(column=1, row=3, padx=5, pady=5)
    submit_buttom.grid(column=0, row=5, columnspan=3)

    matrix_display.grid(column=0, row=4, columnspan=3)


# Sample Matrices
sample1_m1_label = tk.Label(text="Samples for Matrix 1: ")
sample1_m2_label = tk.Label(text="Samples for Matrix 2: ")

sample1_m1_button1 = tk.Button(text="1", command=fill_sample1_m1, height=1)
sample1_m2_button1 = tk.Button(text="1", command=fill_sample1_m2, height=1)

# Inputs
input1_label = tk.Label(text="Enter the first matrix: ")
input1 = tk.Entry()

input2_label = tk.Label(text="Enter the second matrix: ")
input2 = tk.Entry()

# Showing the matrices
show_matrix1 = tk.Label(text="Default Matrix 1:\n "
                             """[1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]""")
show_matrix2 = tk.Label(text="Default Matrix 2:\n "
                             """[1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]""")

# Result Buttons
input_button1 = tk.Button(text="Input", command=show_input_window1, width=5)
input_button2 = tk.Button(text="Input", command=show_input_window2, width=5)
construct_matrix = tk.Button(text="CONSTRUCT MATRICES", command=construct_matrices)
add_button = tk.Button(text="Add", command=add, width=10)
sub_button = tk.Button(text="Subtract", command=sub, width=10)
mul_button = tk.Button(text="Multiply", command=mul, width=10)
det_button = tk.Button(text="Determinant", command=show_dets, width=10)

# Showing the result
result = tk.Label()

# Display Sample Matrices
sample1_m1_label.place(x=5, y=5)
sample1_m2_label.place(x=5, y=30)

sample1_m1_button1.place(x=130, y=5)
sample1_m2_button1.place(x=130, y=25)

# Display Inputs
input1_label.place(x=5, y=60)
input1.place(x=140, y=60)

input2_label.place(x=5, y=85)
input2.place(x=140, y=85)

# Display Input Matrices
show_matrix1.place(x=325, y=20)
show_matrix2.place(x=450, y=20)

# Result Buttons
input_button1.place(x=275, y=60)
input_button2.place(x=275, y=85)
construct_matrix.place(x=130, y=105)
add_button.place(x=5, y=150)
sub_button.place(x=5, y=180)
mul_button.place(x=5, y=210)
det_button.place(x=5, y=240)

# Show Result
result.place(x=325, y=150)

window.mainloop()
