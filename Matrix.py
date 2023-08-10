class Matrix:
    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def print_matrix(self):
        matrix_rows = [self.r1, self.r2, self.r3]
        for row in matrix_rows:
            print(row)


class OperateMatrix:
    def __init__(self, matrix1, matrix2):
        self.m1 = matrix1
        self.m2 = matrix2

    def add_matrix(self):
        m1 = self.m1
        m2 = self.m2

        r1 = [m1.r1[0] + m2.r1[0], m1.r1[1] + m2.r1[1], m1.r1[2] + m2.r1[2]]
        r2 = [m1.r2[0] + m2.r2[0], m1.r2[1] + m2.r2[1], m1.r2[2] + m2.r2[2]]
        r3 = [m1.r3[0] + m2.r3[0], m1.r3[1] + m2.r3[1], m1.r3[2] + m2.r3[2]]
        new_matrix = Matrix(r1, r2, r3)
        return new_matrix
