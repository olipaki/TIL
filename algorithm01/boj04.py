
# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
#############################################################
# 각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 
# 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
# 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
###########################################################

# #from collections import deque

# # w: 다리 길이, L: 최대 하중, trucks: 트럭들 무게 리스트
# def solution(w, L, trucks):
#     trucks = deque(trucks) # 대기 트럭
#     bridge = deque([0] * w) # 다리 상태 (처음엔 0으로 가득 참)
#     time = 0
#     current_weight = 0 # 현재 다리 위 무게 (계속 더하면 느리니까 따로 관리해요)

#     while trucks:
#         time += 1
#         # 1. 다리에서 나가는 차 빼기
#         current_weight -= bridge.popleft()

#         # 2. 새 트럭이 들어올 수 있나?
#         if current_weight + trucks[0] <= L:
#             new_truck = trucks.popleft()
#             bridge.append(new_truck)
#             current_weight += new_truck
#         else:
#             # 못 들어오면 0을 넣어서 전진시키기
#             bridge.append(0)

#     # 마지막 트럭이 올라가고 반복문이 끝나므로, 다리 길이만큼 더해주면 끝!
#     return time + w
################ 선생님 답변###############################################
    from collections import deque

while True:
    data = input()
    braket_dic = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
        '>' : '<'
    }
    open_braket = set(braket_dic.values())
    close_braket = braket_dic.keys()

    if data == '.':
        break

    stack = deque()
    is_valid = True

    for s in data:
        if s in open_braket:
            stack.append(s)

        elif s in close_braket:
            if stack and stack[-1] == braket_dic[s]:
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False
    
    if is_valid:
        print('yes')
    else:
        print('no')
