
num = int(input())

#st = list(map(str,input().split()))

for i in range(num):
    st = input()
    st = st.upper()
    size = len(st)
    for j in range(size//2):
        if st[j] !=st[-j-1]:
            print("#",i+1," NO")
            break
    else:
        print("#",i+1," YES")
            
