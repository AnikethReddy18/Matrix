from Matrix import Matrix, OperateMatrix
import tkinter as tk


def get_inputs():
    i1 = input1.get()
    i2 = input2.get()

    matrix1 = Matrix()
    matrix1.construct_matrix(i1)
    matrix2 = Matrix()
    matrix2.construct_matrix(i2)

    show_matrix.config(text=f"{matrix1}and\n{matrix2} are your input matrices")


window = tk.Tk()

instructions = tk.Label(text="To make a matrix: Enter 9 numbers of your choice separated by a comma" \
                             "and no space. They will be filled left to right starting from top to bottom")

input1 = tk.Entry()
input2 = tk.Entry()
show_matrix = tk.Label()
show_button = tk.Button(text="Show Matrices", command=get_inputs)

instructions.pack()
input1.pack()
input2.pack()
show_button.pack()
show_matrix.pack()

window.mainloop()
