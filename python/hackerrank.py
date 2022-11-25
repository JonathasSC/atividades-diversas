# participantes = {
#     'alice':0,
#     'bob':0
# }

# def compareTriplets(a,b):
#     for pontos in range(0,3):
#         if a[pontos] > b[pontos]:
#             participantes['alice'] += 1
#         if a[pontos] < b[pontos]:
#             participantes['bob'] += 1
#         else:
#             pass        
#     return list(participantes.values())

# print(compareTriplets([17,28,30],[99,16,8]))



# def aVeryBigSum(ar):
#      return (sum(ar))
# print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))


def diagonalDifference(arr):
    n = len(arr)    # left_diag  =  [ arr [ i ][ i ]  for  i  in  range ( 0 , len ( arr ))] 
    # right_diag  =  [ arr [ i ][ ~ i ]  for  i  in  range ( 0 , len ( arr ) )] 
    # return  ( sum( left_diag ) - sum( right_diag ))

    n = len(arr)

    assert n == len(arr[0])

    reverse = list(reversed(arr))
    sum_diagonal = sum(reverse[i][i] for i in range(n))
    sum2_diagonal = sum(arr[i][i] for i in range(n))
    return abs (sum_diagonal - sum2_diagonal)

print(diagonalDifference([[11,2,4,9],[4,5,6,5],[10,8,-12,6],[10,8,-12,6]]))

# diagonal1 = 4
# diagonal2 = 19

# [11, 2, 4]
#  [4, 5, 6]
# [10, 8, -12]