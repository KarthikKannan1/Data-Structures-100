def reverseList(lst):
  print( lst[::-1])
     

lst = list(map(int,input("Enter the array: ").split()))
print(lst)
print("Reversed list is")
reverseList(lst) 