#Updation
promo = [21,"Suleman",3.5,"Karachi"]
print(promo[0])

promo[0] = 56
print(promo[0])


list1 = []
print("Blank list:",list1)

list1 = [24,26,28,37]
print(f"The list of numbers are:{list1}\n")

#1. Append method
list1.append(31)
print(f"After Append Method: {list1}\n")

#2. Slicing
slicing = list1[1:3]
print(f"{slicing}\n") # output = [26,28]

#3. Sorting

## Ascending
new_list = [1,4,7,23,89]
new_list.sort()
print(new_list)

fruits = ["Apple" , "Mango" , "Orange" , "BlueBerry"]
print(f"The length of fruit list is: {len(fruits)}")
fruits.sort()
print(f"The fruits are in ascending order: {fruits}")

## Descensing
fruits.sort(reverse=True)
print(f"The fruits are in descending order: {fruits}")

new_list = [43,56,67]
new_list.sort(reverse=True)
print(f"The sorted list are in descending order: {new_list}\n")


#4. Reversing
new_list = [1,2,3,4,5,6,7,8,9,10]
print(new_list[-1]) # negative indexing (Last Element)
new_list.reverse()
print(f"The reversed list is: {new_list}\n")

#5. Insert Method (can add at any position)

list3 = [1,3,7,9,11]
print(f'The list before insertion: {list3}')
list3.insert(2,5) #First one is index number and second one is value
print(f'The list after insertion: {list3}\n')

#6. Remove Method
Constant = [3.14,9.81,2.71]
print(f'The list before removal: {Constant}')
Constant.remove(2.71)
print(f'The list after removal: {Constant}\n')

#7. Pop Method
animals = ["Wolf","Octupus","Lion","Shark","Dog"]
print(f"Before using pop method: {animals}")
animals.pop(4)
print(f"After using pop method: {animals}\n")

