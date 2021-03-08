# find sum of all even numbers from 1 to 100 including 1 and 100
sum_even_number_till_100 = 0

# Get the range from the user
range_start = int(input("Enter the starting range of number. For e.g. for 1 - 100 enter 1  :"))
range_end = int(input("Enter ending range of the number For e.g. for 1 to 100 enter 101    :"))

# Check if even number then add to the aggregator
for number in range(1, 101):
    if ((number%2) == 0):
        sum_even_number_till_100 += number

print(f"The sum of numbers of the range is {sum_even_number_till_100}")
