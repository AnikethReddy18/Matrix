from Matrix import Matrix, OperateMatrix
import tkinter as tk

matrix1 = Matrix()
matrix2 = Matrix()
operation = OperateMatrix()


def construct_matrices():
    global matrix1, matrix2, operation

    matri1 = Matrix()
    matri1.construct_matrix(input1.get())
    matri2 = Matrix()
    matri2.construct_matrix(input2.get())
    matrix1 = matri1
    matrix2 = matri2

    operation = OperateMatrix(matrix1, matrix2)


def show_matrices():
    show_matrix.config(text=f"{matrix1}and\n{matrix2} are your input matrices")


def add():
    result.config(text=operation.add_matrix())


def sub():
    result.config(text=operation.sub_matrix())


def mul():
    result.config(text=operation.mul_matrix())


window = tk.Tk()

instructions = tk.Label(text="To make a matrix: Enter 9 numbers of your choice separated by a comma\n"
                             "and no space. They will be filled left to right starting from top to bottom")

input1 = tk.Entry()
input2 = tk.Entry()
construct_matrix = tk.Button(text="CONSTRUCT MATRICES", command=construct_matrices)
show_matrix = tk.Label()
show_button = tk.Button(text="Show Matrices", command=show_matrices)
add_button = tk.Button(text="add", command=add)
sub_button = tk.Button(text="subtract", command=sub)
mul_button = tk.Button(text="multiply", command=mul)
result = tk.Label()

instructions.pack()
input1.pack()
input2.pack()
construct_matrix.pack()
show_button.pack()
show_matrix.pack()
add_button.pack()
sub_button.pack()
mul_button.pack()
result.pack()

window.mainloop()
