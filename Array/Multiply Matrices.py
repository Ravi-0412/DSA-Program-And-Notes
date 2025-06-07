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

# Java Code
"""
import java.util.*;

class Solution {
    public int[][] matrixMultiplication(int[][] A, int[][] B) {
        // Get the number of rows and columns of the input matrices
        int rows_A = A.length, cols_A = A[0].length;
        int rows_B = B.length, cols_B = B[0].length;

        // Ensure matrices A and B can be multiplied
        if (cols_A != rows_B) {
            throw new IllegalArgumentException("Number of columns in A must be equal to the number of rows in B");
        }

        // Initialize the result matrix with zeros
        int[][] result = new int[rows_A][cols_B];

        // Perform matrix multiplication
        for (int i = 0; i < rows_A; i++) {
            for (int j = 0; j < cols_B; j++) {
                for (int k = 0; k < cols_A; k++) {
                    result[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return result;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <stdexcept>

using namespace std;

vector<vector<int>> matrixMultiplication(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    // Get the number of rows and columns of the input matrices
    int rows_A = A.size(), cols_A = A[0].size();
    int rows_B = B.size(), cols_B = B[0].size();

    // Ensure matrices A and B can be multiplied
    if (cols_A != rows_B) {
        throw invalid_argument("Number of columns in A must be equal to the number of rows in B");
    }

    // Initialize the result matrix with zeros
    vector<vector<int>> result(rows_A, vector<int>(cols_B, 0));

    // Perform matrix multiplication
    for (int i = 0; i < rows_A; i++) {
        for (int j = 0; j < cols_B; j++) {
            for (int k = 0; k < cols_A; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}
"""