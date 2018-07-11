def O(num):
    if len(num) == 0:
        return 0
    l=0
    r=len(num)-1
    mid = 0
    while num[l]>=num[r]:
        if r-l ==1:
            mid = r
            break
            # return num[r]

        mid = l + (r-l)//2
        if num[mid]==num[l] and num[mid]==num[r]:
            return OO(num,l,r)
        if num[mid]>=num[l]:
            l=mid
        else:
            r=mid

    return num[mid]

def OO(num,l,r):
    result = num[l]
    for i in range(l+1,r):
        if result > num[i]:
            result=num[i]
    return result

num =[1,1,0,1,1,119]
print(O(num))