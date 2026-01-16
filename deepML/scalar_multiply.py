#https://www.deep-ml.com/problems/5?from=Linear%20Algebra
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = []
    for row in matrix:
        temp=[]
        for elem in row:
            temp.append(scalar*elem)
        result.append(temp)
    return(result)
