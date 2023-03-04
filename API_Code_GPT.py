#write a code to find determinant of a matrix of nxn using recursion

def determinant(matrix): 
    n = len(matrix) 

    # Base case for 2x2 matrix 
    if n == 2: 
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0] 

    det = 0
    for c in range(n): 
        sub_matrix = [] 
        for r in range(1, n): 
            temp_row = []  
            for j in range(n):  
                if j != c:  
                    temp_row.append(matrix[r][j])  

            sub_matrix.append(temp_row)  

        sign = (-1) ** (c % 2)  
        sub_det = determinant(sub_matrix)  

        det += sign * matrix[0][c] * sub_det  

    return det