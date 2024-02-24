def sum_of_list(num):
  return sum(int(i) for i in str(num))


list1 = [987, 456, 345, 321, 654, 879, 346, 574, 859]
sum_list= []
sum_list = [sum_of_list(j) for j in list1]

print(f"sum of the digits of numbers in a list : {sum_list}")