#1.Write a program script to merge two python dictionaries
dict1={1:"apple",2:"orange",3:"banana",4:"mango"}
print("dict1 is: ",dict1)
dict2={5:"pineapple",6:"strawberry",7:"kiwi"}
print("dict2 is :",dict2)
dict2.update(dict1)
print("After merging dict1 & dict2: ",dict2)


#2.write a program to sort the value from descending to ascending in list and convert into a set
list1=[10,4,7,8,29,48,9]
print("list1 is: ",list1)
list1.sort()
print("After sorting from descending to ascending: ",list1[::-1])
print("After converting list into set: ",set(list1))

#3.write a python program to list number of items in a dictionary key and sort the list with the help of a function $ without the function
def function1(new_dict):
    res = dict()
    for key in sorted(new_dict):
        res[key] = sorted(new_dict[key])
    return res
print("Sorting dict")
new_dict={"apple":'1',"orange":'2',"banana":'3',"mango":'4'}
print("The new_dict is: ",new_dict)
print("The number of items in new_dict: ",len(new_dict.keys()))
print("sorted dict",function1(new_dict))

#4.write a python program to get a string from a given string(user input) and change the first occcurence of the word to a user specified input
string = input("Enter the string: ")
word = input("Enter the word to replace: ")
print("The changed string is: ",string.replace(string.split()[0],word))

#5.write a python program to get a string from a given string where all occurences of its first char have been  changed to capital letter
print("After changing all first characters to capital letters: ",string.title())

#6.write a python program to find the repeated items in a list
list2=[5,4,3,6,4,2,9,8,5,3]
print("list2 is: ")
rep=[]
for i in list2:
    if list2.count(i)>1:
        rep.append(i)
print("Repeated items in list2: ",list(set(rep)))

#7.write a python program to check the sum of three elements and divided by a value which is given as input by the user
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
inp=int(input("Enter the number to divide: "))
print("Answer is: ",(a+b+c)//inp)

#8.write a python program to find the mean, median, mode among three given numbers
list3=[]
for i in range(3):
    list3.append(int(input("Enter the numbers for list3: ")))
print("list3 is: ",list3)

mean=sum(list3)//3
print("Mean for list3 is: ",mean)

sort=sorted(list3)
print("Median for list3 is: ",sort[1])

l1=[]
for i in range(3):
  l1.append(list3.count(list3[i]))
d1=dict(zip(list3,l1))
d2={k for (k,v) in d1.items() if v==max(l1)}
if len(d2)==len(list3):
    print("No Mode")
else:
    print("The mode for list3 is: ",d2)

#9.write a pyhton program to swap cases of a given string
print("After swaping cases of string: ",string.swapcase())

#10.write a program to convert an integer to binary & octa decimal
number=int(input("Enter the number to convert: "))
print("Binary value of number is: ",bin(number))
print("Octa decimal value of number is: ",oct(number))

