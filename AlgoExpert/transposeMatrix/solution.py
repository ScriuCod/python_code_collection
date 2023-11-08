
# O(w * h)time | O(w * h)space
def transposeMatrix(matrix):
    transposed_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)
    return transposed_matrix
