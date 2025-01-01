# Define the function
def multiplyTwoMatrices(A, B):
    # Checking if the two matrices can be multiplied
    if len(A[0]) != len(B):
        raise ValueError("The number of Columns of Matrix A does not match the number of rows of matrix B")
        Break

    # Get the dimensions
    rows_A = len(A)
    cols_B = len(B[0])
    cols_A = len(A[0]) # This is the same for the rows of B

    # initialize the resulting matrix with zeros
    results = [[0 for _ in range(cols_A)] for _ in range(rows_A)]

    # Matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            results[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))

    return results