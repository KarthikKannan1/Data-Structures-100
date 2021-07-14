def insert(arr, element):
    arr.append(element)
    arr.sort()

arr = list(map(int,input("Enter the elements in your array: ").split()))
key = int(input("Enter the element that you want to insert: "))

print ("Before Inserting: ")
print (arr)

insert(arr, key)
print("After Inserting: ")
print (arr)