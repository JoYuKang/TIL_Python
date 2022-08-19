
from collections import deque
import sys
# num = int(sys.stdin.readline().strip())

# result = ""
# for k in range(num):
#     strArr = sys.stdin.readline().strip()
#     arrLen = int(sys.stdin.readline().strip())
#     check = False
#     temp =  sys.stdin.readline().strip()[1:-1].split(",")
#     count = 0
    
#     queue = deque(temp)
    
#     if arrLen == 0:
#         queue = deque()


#     for i in strArr:
#         if i == "D":
#             try :
#                 if count % 2 == 0:
#                     queue.popleft()
#                 else:
#                     queue.pop()
#             except :
#                 check = True
#                 result += "error\n"
#                 break
#         elif i == "R":
#             count += 1
#     if check == False:
#         if count % 2 == 0:
#             result += f'{list(map(int, queue))}\n'
#         else:
#             result += f'{list(map(int, reversed(queue)))}\n'

# print(result)

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")