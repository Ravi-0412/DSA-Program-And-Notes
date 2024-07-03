# Time = rows_A * cols_B * cols_A

def matrix_multiplication(A, B):
    # Get the number of rows and columns of the input matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Ensure matrices A and B can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to the number of rows in B")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Java
public class MatrixMultiplication {

    public static int[][] multiplyMatrices(int[][] A, int[][] B) {
        int rowsA = A.length;
        int colsA = A[0].length;
        int rowsB = B.length;
        int colsB = B[0].length;
        
        if (colsA != rowsB) {
            throw new IllegalArgumentException("Number of columns in A must be equal to the number of rows in B");
        }
        
        int[][] result = new int[rowsA][colsB];
        
        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    result[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        
        return result;
    }
}