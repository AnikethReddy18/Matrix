from Matrix import Matrix, OperateMatrix
import tkinter as tk

window = tk.Tk()
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

    #show_matrices.config(text=f"Your matrices will be displayed here:\n{matrix1}{matrix2} ")
    print(matrix1)
    operation = OperateMatrix(matrix1, matrix2)


def add():
    result.config(text=operation.add_matrix())


def sub():
    result.config(text=operation.sub_matrix())


def mul():
    result.config(text=operation.mul_matrix())


# Inputs
input1_label = tk.Label(text="Enter the first matrix: ")
input1 = tk.Entry()
input1.insert(0, "1,2,3,4,5,6,7,8,9")

input2_label = tk.Label(text="Enter the second matrix: ")
input2 = tk.Entry()
input2.insert(0, "1,2,3,4,5,6,7,8,9")

# Showing the matrices
show_matrix1 = tk.Label(text="Default Matrix 1:\n "
                             """[1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]""")
show_matrix2 = tk.Label(text="Default Matrix 2:\n "
                             """[1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]""")

# Buttons
construct_matrix = tk.Button(text="CONSTRUCT MATRICES", command=construct_matrices)
add_button = tk.Button(text="Add", command=add, width=10)
sub_button = tk.Button(text="Subtract", command=sub, width=10)
mul_button = tk.Button(text="Multiply", command=mul, width=10)

# Showing the result
result = tk.Label()




# Display Inputs
input1_label.place(x=5, y=40)
input1.place(x=140, y=40)

input2_label.place(x=5, y=65)
input2.place(x=140, y=65)

# Display Input Matrices
show_matrix1.place(x=325, y=20)
show_matrix2.place(x=450, y=20)

# Buttons
construct_matrix.place(x=140, y=85)
add_button.place(x=5, y=150)
sub_button.place(x=5, y=180)
mul_button.place(x=5, y=210)

# Show Result
result.place(x=325, y=150)

window.mainloop()
