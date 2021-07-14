def findElement(arr, n, key):
    for i in range (n):
        if (arr[i] == key):
            return i
    return -1

arr = list(map(int,input("Enter the elements of the array: ").split()))
n = len(arr)
key = int(input("Enter the element you want to find the position of: "))

index = findElement(arr, n, key)
if index != -1:
    print ("Element found at position: " + str(index + 1 ))
else:
    print ("Element not found")