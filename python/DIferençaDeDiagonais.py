def diagonalDifference(arr):

    # left_diag  =  [ arr [ i ][ i ]  for  i  in  range ( 0 , len ( arr ))] 
    # right_diag  =  [ arr [ i ][ ~ i ]  for  i  in  range ( 0 , len ( arr ) )] 
    # return  ( sum( left_diag ) - sum( right_diag ))

    n = len(arr)

    assert n == len(arr[0])

    reverse = list(reversed(arr))
    sum_diagonal = sum(reverse[i][i] for i in range(n))
    sum2_diagonal = sum(arr[i][i] for i in range(n))
    return abs (sum_diagonal - sum2_diagonal)

print(diagonalDifference([[11,2,4,9],[4,5,6,5],[10,8,-12,6],[10,8,-12,6]]))