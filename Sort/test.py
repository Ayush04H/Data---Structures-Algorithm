def bubble(l):
    n=len(l)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if l[min_ind] > l[j]:
                min_ind = j

        l[min_ind],l[i] = l[i],l[min_ind]
        

            


arr =[1,2,3,4,5,9,6,7,8]
bubble(arr)
print(arr)