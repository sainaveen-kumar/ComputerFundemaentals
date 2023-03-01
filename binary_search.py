pos=-1
def search(list,n):
    l=0;
    u=len(list)-1;
    while l<=n:
        mid=(l+u)//2;
        if list[mid]==n:
            
            return mid+1
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid
l=[int(i) for i in input().split()]
n=int(input())
print(search(l,n))
