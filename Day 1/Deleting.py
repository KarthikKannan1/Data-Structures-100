arr = list(map(int,input("Please enter the elements of your array: ").split()))
n = len(arr)
key = int(input("Please enter the element which you wish to delete: "))
  
print("\nArray before deletion:")
print (arr)

print("\nArray after deletion")
for i in range(n):
    if (arr[i] == key):
        arr.remove(key)
        print(arr)
        break
else:
    print("Element not present")