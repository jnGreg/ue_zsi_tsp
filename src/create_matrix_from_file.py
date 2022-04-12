

class Matrix:

    def __init__(self, file_path):
        self.file_path = file_path

    def create_matrix(self) -> [[]]:
        matrix = []

        with open(self.file_path, "r") as file:
            [matrix.append(list(map(int, line.split()))) for line in file.readlines()[1:]]
        file.close()

        for index, element in enumerate(matrix):
            row = index + 1
            for _ in range(len(matrix) - row):  # make the matrix symmetric
                element.append(matrix[row][index])
                row += 1

        return matrix
