# loops in python
# for Loop
# for each loop
# whileloop


friendname=["Neha","Garima","Hardik"]
print("before",friendname)
friendname.append("Dil bhardwaj")
print("after",friendname)
friendname.insert(0,"Harsh")
friendname.insert(3,"harsh")
print("add name at index 0",friendname)
friendname.remove("Harsh")
print(friendname)
#to clear the list
# friendname.clear()
# print(friendname)
friendname.pop(2)
print(friendname)
#to remove the data in list with specific index
friendname.sort()
print(friendname)
#to print element in the given list
for names in friendname:
    print(names)
    
#to print the 1 to 10   
#for(int x=0;x<11;x++)
for i in range(1,11):
    print(i) 
#to even no
print("even no")
for i in range(1,11):
    if i % 2==0:
        print(i)
        
print("Tuple set") 
sets={"Neha","Mayank","Garima","Neha"}
sets.add("Harsh")
sets.remove("Harsh")
print(sets)
print(type(sets))       

list=["neha","suhana","garima","hardik","dil"]
print(list)
list.sort(reverse=True)
print(list)
    