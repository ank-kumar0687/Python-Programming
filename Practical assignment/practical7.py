
list1 = ['physics', 'chemistry', '1997', '2000']
list2 = [1, 2, 3, 4, 5, 6, 7]

# i List Concatenation
list3 = list1 + list2
print("Concatenation:", list3)

# ii Remove list1[3]
list1.pop(3)
print("After removing list1[3]:", list1)

# iii Add Java in list1
list1.append("Java")
print("After adding Java:", list1)

# iv Update list2 as list2[3] = 11
list2[3] = 11
print("After updating list2:", list2)

# v del list2[2]
del list2[2]
print("After deleting list2[2]:", list2)

# vi Print message 4 times

for i in range(4):
    print("Welcome to Marwadi University")

# vii Slicing operations

print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])

# viii Length of list2

print("Length of list2:", len(list2))

# ix Maximum element in list1

print("Maximum element in list1:", max(list1))

# x Minimum element in list2

print("Minimum element in list2:", min(list2))

# xi list2.append(100)

list2.append(100)
print("After append 100:", list2)

# xii. Extend operation

list2.extend([200, 300])
print("After extend:", list2)

# xiv Difference between pop and remove

list2.pop()          
list2.remove(11)    
print("After pop and remove:", list2)

# xv Reverse list1

list1.reverse()
print("Reversed list1:", list1)

# xvi Descending order in list2

list2.sort(reverse=True)
print("Descending list2:", list2)