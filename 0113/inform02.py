# 1,5,9,13/2,6,10,14 줄 세로로 출력해보기

mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]


for j in range(4):# 행(가로 위치)
    for i in range(4): #열(세로 위치)
        print(mat[i][j],end=" ")

        # 세로로 출력
# 1  mat[0][0]
# 5  mat[1][0]
# 9  mat[2][0]
# 13 mat[3][0]

# 2  mat[0][1]
# 6  mat[1][1]
# 10 mat[2][1]
# 14 mat[3][1]


# 가장 밖의 for문이라 i로 시작한다 -> X
# mat[i][j]의 형태를 유지한다 -> O
# 더 나중에 헷갈리지 않는 방식이라고 생각합니다.
# for j in range(4):
#     mat[0][j]
#     mat[1][j]
#     mat[2][j]
#     mat[3][j]

for j in range(len(mat[0])):
    for i in range(len(mat)):
        print(mat[i][j])
