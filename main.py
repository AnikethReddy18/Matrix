import tkinter.messagebox

from Matrix import Matrix, OperateMatrix
import tkinter as tk

window = tk.Tk()
window.title("Matrix Calculator")
window.geometry("600x400")

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

    except ValueError:
        tkinter.messagebox.showerror("Value Error", "Please Enter a Valid Input")
        input1.delete(0, "end")
        input2.delete(0, "end")


def add():
    try:
        result.config(text=operation.add_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input")
        input1.delete(0, "end")
        input2.delete(0, "end")


def sub():
    try:
        result.config(text=operation.sub_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input")
        input1.delete(0, "end")
        input2.delete(0, "end")



def mul():
    try:
        result.config(text=operation.mul_matrix())

    except:
        tkinter.messagebox.showerror("Index Error", "Please Enter a Valid Input")
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
construct_matrix.place(x=140, y=105)
add_button.place(x=5, y=150)
sub_button.place(x=5, y=180)
mul_button.place(x=5, y=210)
det_button.place(x=5, y=240)

# Show Result
result.place(x=325, y=150)

window.mainloop()
