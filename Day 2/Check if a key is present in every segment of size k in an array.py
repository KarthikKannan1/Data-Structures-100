def findxinkindowSize(arr, x, k, n) :
 
    i = 0
    while i < n :
 
        j = 0

        while j < k :
             
            if arr[i + j] == x :
                break
             
            j += 1

        if j == k :
            return False
 
        i += k
  
    if i == n :
        return True
 
    j = i - k

    while j < n :
        if arr[j] == x :
            break
 
        j += 1
 
    if j == n :
        return False
 
    return True

if __name__ == "__main__" :
 
    arr = list(map(int,input("Enter an array: ").split()))
    x = int(input("Enter the element you want to check: "))
    k = int(input("Enter the key: "))
    n = len(arr)
     
    if (findxinkindowSize(arr, x, k, n)) :
        print("Yes")
    else :
        print("No")