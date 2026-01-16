mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
# 1. mat[i][j]의 형태를 활용해서
# 1,2,3,4,5,6...16순서대로 출력

# 1. 가로 방향으로 출력 (행 우선 탐색)
# 바깥쪽 반복문: 행(Row) 인덱스 i를 0부터 3까지 바꿉니다.
# 안쪽 반복문: 열(Column) 인덱스 j를 0부터 3까지 바꿉니다.

for i in range(4):# 행(세로 위치)
    for j in range(4): #열(가로위치)
        print(mat[i][j], end=" ")


print(mat[0][0])
print(mat[0][1])
print(mat[0][2])
print(mat[0][3])

i=0
print(mat[i][0])
print(mat[i][1])
print(mat[i][2])
print(mat[i][3])