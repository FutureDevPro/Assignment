#Basic Level



#1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.

for i in range(1,11):
  print(i)

#2. Create a program that calculates the sum of all numbers in a list using a `for` loop.

list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in list:
  sum += i
print(sum)

#3. Write a program to print the characters of a string in reverse order using a `for` loop.

string = "Hey Google"
for i in string[::-1]:
  print(i,end = '')

#4. Develop a program that finds the factorial of a given number using a `for` loop.

num = int(input("Enter a number: "))
for i in range(1,num):
  if num % i == 0:
    print(i)

#5. Create a program to print the multiplication table of a given number using a `for` loop.

num = int(input("Enter a number: "))
for i in range(11):
  print(f"{num} x {i} = {num*i}")

#6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.

list = [1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0
for i in list:
  if i % 2 == 0:
    even += 1
  else:
    odd += 1
print(f"Even: {even}\nOdd: {odd}")

#7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.

for i in range(1,6):
  print(f"square of {i} = {i*i}")

#8. Create a program to find the length of a string without using the `len()` function.

string = input("Enter String ")
count = 0
for i in string:
    count += 1
print(f"length of a {string} is {count}")

#9. Write a program that calculates the average of a list of numbers using a `for` loop.

list1 = [1,4,6,7,3,5,8,9,5,7]
add = 0
for i in list1:
    add += i
average = add/len(list1)

print(f"average of a list is {average}")

 #10. Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.

num = int(input("Enter a number: "))
a = 0
b = 1
for i in range(num):
  print(a)
  c = a + b
  a = b
  b = c




#Intermediate Level:




#11. Write a program to check if a given list contains any duplicates using a `for` loop.

list1 = []
a = int(input("enter no. of items in list: "))
for i in range(a):
  b = int(input(f"Enter {i+1} item : "))
  list1.append(b)

list2 = []
for i in list1:
  if i in list2 :
    print(f"duplicate value {i} ")
  list2.append(i)

#12. Create a program that prints the prime numbers in a given range using a `for` loop.

num = int(input("Enter range : "))
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not prime number")
        break
    else:
        print(f"{num} is prime number")
        break

#13. Develop a program that counts the number of vowels in a string using a `for` loop.

count = 0
string = input('Enter string : ')
for i in string:
    if i in 'aeiou':
        count += 1
print(f"number of vowels : {count}")

#14. Write a program to find the maximum element in a 2D list using a nested `for` loop.

row = int(input("Enter number of row : "))
coloumn = int(input("Enter number of coloumn : "))

list1 = []
for i in range(row):
    list2 = []
    for j in range(coloumn):
        Elelments = int(input(f"Enter {i+1}th {j+1}th element number : "))
        list2.append(Elelments)

    list1.append(list2)

max = 0
for i in list1:
    for j in i:
        if j > max:
            max = j

print(f"maximum element in a 2D list : {max}")


#15. Create a program that removes all occurrences of a specific element from a list using a `for` loop.

string = input("Enter String : ")
list1 = list(string)
new_list = []
print(list1)
element = input("Enter element that you want to remove : ")
for i in list1:
    if i != element:
        new_list.append(i)        

print(new_list)

#16. Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.

for i in range(1,6):
    print(f"Multiplication table of {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

#17. Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.

temp_Cal = []
temp_Fah = [80,100,400,362,250,321,165,175,277]
for i in temp_Fah:
     Cal = (i - 32) * 5/9
     temp_Cal.append(Cal)

print(f"list of Fahrenheit temperatures to Celsius : {temp_Cal}")

#18. Create a program to print the common elements from two lists using a `for` loop.

common_elements = []

list1 = [5,6,4,8,4,7,1,9,4,6,9,3,45,11]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in list1:
    if i in list2:
      if i not in common_elements:
        common_elements.append(i)

print(f"Common elements are : {common_elements}")

#19. Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the pattern

row = int(input("Enter rows of stars : "))
for i in range(row):
    print((i+1)*'*')

#20. Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.

num1_divisor = []
num2_divisor = []
common_divisor = []

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

for i in range(1,num1+1):
    if num1 % i == 0:
        num1_divisor.append(i)

for j in range(1,num2+1):
    if num2 % j == 0:
        num2_divisor.append(j)

for i in num1_divisor:
    if i in num2_divisor:
        common_divisor.append(i)

max=0
for i in common_divisor:
    if i>max:
        max=i

print(f"greatest common divisor (GCD) of two numbers : {max}")



