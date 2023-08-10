class Matrix:
    def __init__(self, r1=None, r2=None, r3=None):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def print_matrix(self):
        matrix_rows = [self.r1, self.r2, self.r3]
        for row in matrix_rows:
            print(row)

    def element(self, column=1, row=1):
        r1 = self.r1
        r2 = self.r2
        r3 = self.r3

        element = None
        if row == 1:
            element = r1[column - 1]
        elif row == 2:
            element = r2[column - 1]
        elif row == 3:
            element = r3[column - 1]

        return element

    def make_matrix(self, numbers):
        """PUT IN A STRING OF NUMBER SEPARATED BY A COMMA AND NO SPACES """
        matrix_fr = numbers.split(',')
        self.r1 = matrix_fr[:3]
        self.r2 = matrix_fr[3:6]
        self.r3 = matrix_fr[6:9]


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

    def sub_matrix(self):
        m1 = self.m1
        m2 = self.m2

        r1 = [m1.r1[0] - m2.r1[0], m1.r1[1] - m2.r1[1], m1.r1[2] - m2.r1[2]]
        r2 = [m1.r2[0] - m2.r2[0], m1.r2[1] - m2.r2[1], m1.r2[2] - m2.r2[2]]
        r3 = [m1.r3[0] - m2.r3[0], m1.r3[1] - m2.r3[1], m1.r3[2] - m2.r3[2]]

        new_matrix = Matrix(r1, r2, r3)
        return new_matrix
