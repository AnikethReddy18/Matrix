from Matrix import Matrix, OperateMatrix
import tkinter as tk

window =tk.Tk()
window.title("Matrix Calculator")
window.geometry("600x400")

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

    show_matrix.config(text=f"{matrix1}and\n{matrix2} are your input matrices")

    operation = OperateMatrix(matrix1, matrix2)


def add():
    result.config(text=operation.add_matrix())


def sub():
    result.config(text=operation.sub_matrix())


def mul():
    result.config(text=operation.mul_matrix())



instructions = tk.Label(text="To make a matrix: Enter 9 numbers of your choice separated by a comma\n"
                             "and no space. They will be filled left to right starting from top to bottom")

input1 = tk.Entry()
input2 = tk.Entry()
construct_matrix = tk.Button(text="CONSTRUCT MATRICES", command=construct_matrices)
show_matrix = tk.Label()
add_button = tk.Button(text="add", command=add)
sub_button = tk.Button(text="subtract", command=sub)
mul_button = tk.Button(text="multiply", command=mul)
result = tk.Label()

instructions.grid(column=0,row=0)
input1.grid(column=0, row=1, sticky="w")
input2.grid(column=0, row=2, sticky="w")
construct_matrix.grid(column=0, row=3, sticky="w")
show_matrix.grid(column=1,row=1)
add_button.grid(column=0, row=4, sticky="w")
sub_button.grid(column=0, row=5, sticky="w")
mul_button.grid(column=0, row=6, sticky="w")
result.grid(column=1, row=4)

window.mainloop()
