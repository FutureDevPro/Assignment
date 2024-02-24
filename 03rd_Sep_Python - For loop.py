#Basic Level

#1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.

for i in range(1, 11):
  print(i)

#2. Create a program that calculates the sum of all numbers in a list using a `for` loop.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list:
  sum += i
print(sum)

#3. Write a program to print the characters of a string in reverse order using a `for` loop.

string = "Hey Google"
for i in string[::-1]:
  print(i, end='')

#4. Develop a program that finds the factorial of a given number using a `for` loop.

num = int(input("Enter a number: "))
for i in range(1, num):
  if num % i == 0:
    print(i)

#5. Create a program to print the multiplication table of a given number using a `for` loop.

num = int(input("Enter a number: "))
for i in range(11):
  print(f"{num} x {i} = {num*i}")

#6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0
odd = 0
for i in list:
  if i % 2 == 0:
    even += 1
  else:
    odd += 1
print(f"Even: {even}\nOdd: {odd}")

#7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.

for i in range(1, 6):
  print(f"square of {i} = {i*i}")

#8. Create a program to find the length of a string without using the `len()` function.

string = input("Enter String ")
count = 0
for i in string:
  count += 1
print(f"length of a {string} is {count}")

#9. Write a program that calculates the average of a list of numbers using a `for` loop.

list1 = [1, 4, 6, 7, 3, 5, 8, 9, 5, 7]
add = 0
for i in list1:
  add += i
average = add / len(list1)

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
  if i in list2:
    print(f"duplicate value {i} ")
  list2.append(i)

#12. Create a program that prints the prime numbers in a given range using a `for` loop.

num = int(input("Enter range : "))
for i in range(2, num):
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

for i in range(1, 6):
  print(f"Multiplication table of {i}")
  for j in range(1, 11):
    print(f"{i} x {j} = {i*j}")

#17. Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.

temp_Cal = []
temp_Fah = [80, 100, 400, 362, 250, 321, 165, 175, 277]
for i in temp_Fah:
  Cal = (i - 32) * 5 / 9
  temp_Cal.append(Cal)

print(f"list of Fahrenheit temperatures to Celsius : {temp_Cal}")

#18. Create a program to print the common elements from two lists using a `for` loop.

common_elements = []

list1 = [5, 6, 4, 8, 4, 7, 1, 9, 4, 6, 9, 3, 45, 11]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in list1:
  if i in list2:
    if i not in common_elements:
      common_elements.append(i)

print(f"Common elements are : {common_elements}")

#19. Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the pattern

row = int(input("Enter rows of stars : "))
for i in range(row):
  print((i + 1) * '*')

#20. Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.

num1_divisor = []
num2_divisor = []
common_divisor = []

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

for i in range(1, num1 + 1):
  if num1 % i == 0:
    num1_divisor.append(i)

for j in range(1, num2 + 1):
  if num2 % j == 0:
    num2_divisor.append(j)

for i in num1_divisor:
  if i in num2_divisor:
    common_divisor.append(i)

max = 0
for i in common_divisor:
  if i > max:
    max = i

print(f"greatest common divisor (GCD) of two numbers : {max}")

#Advanced Level:

#21. Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.


def sum_of_list(num):
  return sum(int(i) for i in str(num))


list1 = [987, 456, 345, 321, 654, 879, 346, 574, 859]

sum_list = [sum_of_list(j) for j in list1]

print(f"sum of the digits of numbers in a list : {sum_list}")

#22. Write a program to find the prime factors of a given number using a `for` loop and list comprehension.


def prime(num):

  factor = [i for i in range(2, num) if num % i == 0]

  prime_factor = [
    j for j in factor if all(j % k != 0 for k in range(2,
                                                       int(j**0.5) + 1))
  ]

  print(prime_factor)


number = int(input("Enter Number : "))
prime(number)

#23. Develop a program that extracts unique elements from a list and stores them in a new list using a list comprehension.

list1 = [
  1, 3, 5, 7, 9, 0, 8, 6, 4, 2, 1, 5, 0, 4, 7, 45, 87, 2, 4, 8, 6, 35, 354,
  224, 44
]

new_list = list(set([i for i in list1]))

print(new_list)

#24. Create a program that generates a list of all palindromic numbers up to a specified limit using a list comprehension.


def palindromic(num):
  string = str(num)
  rev_string = string[::-1]
  return string == rev_string


def generate(limit):
  list1 = [i for i in range(limit) if palindromic(i)]
  return list1


limit = int(input("Enter Number : "))
num_limit = generate(limit)
print(f"palindromic numbers up to a specified limit : {num_limit}")

#25. Write a program to flatten a nested list using list comprehension.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 6]]

faltten_list = [item for sublist in nested_list for item in sublist]

print(f"Nested List : {nested_list}")

print(f"Flatten List : {faltten_list}")

#26. Develop a program that computes the sum of even and odd numbers in a list separately using list comprehension.

list1 = [
  47, 5, 55, 65, 47, 680, 988, 765, 434, 567, 8, 90, 0, 9, 8, 7, 6, 54, 3, 22,
  45, 6, 7
]

odd_list = [odd for odd in list1 if odd % 2 != 0]

even_list = [even for even in list1 if even % 2 == 0]

print(f"Odd list : {odd_list}")

print(f"Even list : {even_list}")

#27. Create a program that generates a list of squares of odd numbers between 1 and 10 using list comprehension.

odd_sq = [(odd * odd) for odd in range(1, 11) if odd % 2 != 0]

print(f"list of squares of odd numbers : {odd_sq}")

#28. Write a program that combines two lists into a dictionary using list comprehension.

list_key = list("startup")
list_value = [2, 5, 4, 6, 8, 5, 9]

dict_ = {key: value for key, value in zip(list_key, list_value)}

print(f"combines two lists into a dictionary : {dict_}")

#29. Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.



#30. Create a program that removes all non-numeric characters from a list of strings using list comprehension.

string = ["hj64", "d652", "hgd784", "kf784", "jhdcg8u74e5u"]

numeric = [int("".join(filter(str.isdigit, item))) for item in string]

print(f"removes all non-numeric characters from a list : {numeric}")



#Challenge Level:




#31. Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list comprehension.

def Eratosthenes(limit):
    prime = [True] * (limit+1)
    prime[0] = prime[1] = False

    for i in range(2,int(limit ** 0.5)+1):
        if prime[i]:
            prime[i*i:limit+1:i] = [False] * len(prime[i*i:limit+1:i])

    return [i for i in range(2,limit+1) if prime[i]]

limit = int(input("Enter Limit : "))
prime_no = Eratosthenes(limit)
print(f"list of prime numbers of {limit} : {prime_no}")

#32. Create a program that generates a list of all Pythagorean triplets up to a specified limit using list comprehension.

limit = 30

triplets = [(a,b,c) for a in range(1,limit) for b in range(a,limit) for c in range(b,limit) if (a**2 + b**2 == c**2) ]

print(f"Pythagorean triplets up to a specified limit : {triplets}")        

#33. Develop a program that generates a list of all possible combinations of two lists using list comprehension.

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [76,54,32,11,13,35,57,79]
combinations = [(i,j) for i in list1 for j in list2]

print(f"list of all possible combinations of two lists : {combinations}")

#34. Write a program that calculates the mean, median, and mode of a list of numbers using list comprehension.

from collections import Counter

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def calculate_mode(numbers):
    frequency = Counter(numbers)
    max_frequency = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_frequency]

#35. Create a program that generates Pascal's triangle up to a specified number of rows using list comprehension.

def generate_triangle(rows):
    triangle = [[1] * (i+1) for i in range(rows)]
    for i in range(2,rows):
        for j in range(1,i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle

def design_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str , row )).center(len(triangle[-1])*4))

rows = int(input("enter rows : "))

print(generate_triangle)
print(design_triangle(generate_triangle(rows)))


#36. Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using list comprehension.

def factorial(n):

    if n == 0:
        return 1

    else:
        return n* factorial(n-1)

sum = [sum(int(digit) for digit in str(factorial(i))) for i in range(1,6)]

print(f"the sum of the digits of a factorial of numbers from 1 to 5 : {sum}")

#37. Write a program that finds the longest word in a sentence using list comprehension.

string = "How are you What are you doing responsible person"

list1 = list(string.split())

longest = [max(list1 , key=len)]

print(f"the longest word in a sentence : {longest}")

#38. Create a program that filters a list of strings to include only those with more than three vowels using list comprehension.

def count(string):
    vowel = "aeiouAEIOU"
    return sum(1 for char in string if char in vowel)

list1 = ["fukdcjdcaeIOxhyxs" , "jvkmfjhfcgvtIOUafgcv" , "jgfhbjkjhAZEOingfcxvbjk" , "uygtfsswertjhkmnhbvcxdfgh" , "yutgfc" ,"aeiou"]

list_str = [string for string in list1 if count(string) > 3]

print(list_str)

#39. Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list comprehension.

sum_digit = [sum(sum(int(digit) for digit in str(num)) for num in range(1,1001)) ]

print(sum_digit)

#40. Write a program that generates a list of prime palindromic numbers using list comprehension.

def is_prime(limit):
    if limit < 2:
        return False

    for i in range(2,int(limit**0.5)+1):
        if limit % i == 0:
            return False

    return True

limit = 1000
prime_palindromic = [i for i in range(1,limit) if is_prime(i) and str(i) == (str(i))[::-1]  ]

print(f"list of prime palindromic numbers : {prime_palindromic}")